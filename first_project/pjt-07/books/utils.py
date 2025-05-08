import requests
import pickle
from  openai import OpenAI
from pathlib import Path
from django.conf import settings
import uuid
from sklearn.metrics.pairwise import cosine_similarity

emb_API_KEY = 'up_VFfKpHPe17rAGRAKk40AwxtnzWOMb'
CACHE_PATH = Path("book_vectors.pkl")
BATCH_SIZE = 100 

def generate_image_with_openai(thread_title, thread_content, book_title, book_author):

    keyword_extractor_prompt = (
        f"""
        {book_author}의 책 {book_title}을 읽고 쓴 독서 다이어리의 감정을 분석해 키워드 5개를 추출하시오.
        키워드 추출이 완료됐다면 키워드를 기반으로 이미지 생성 AI에 제공할 프롬프트를 작성하시오.
        해당 프롬프트를 통해 해당 독서 다이어리 페이지의 썸네일 이미지를 생성 예정.
        생성할 최종 이미지는 추상적이고 모호한 형태의 초현실주의적인 그림이어야 함. 

        <독서 다이어리>
            <제목>{thread_title}</제목>
            <본문>{thread_content}</본문>
        </독서 다이어리>

        <답변 예시>
            불안, 격정, 찬란함, 노스텔지아, 희망이 담긴 Abstract expressionism 스타일의 추상화
        </답변 예시>

        답변 : 
        """
    )
    client = OpenAI(api_key="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")
    keyword_extractor_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "당신은 이미지 생성 AI를 위한 프롬프트 작성 비서입니다."},
            {"role": "user", "content": keyword_extractor_prompt},
        ],
        max_tokens=2040,
        temperature=0.5
    )
    keyword_extractor_response = keyword_extractor_response.choices[0].message.content
    
    img_generator_prompt = keyword_extractor_response + " 어떠한 텍스트, 글자, 숫자, 심볼도 포함하지 않을 것"
    print(img_generator_prompt)

    response = client.images.generate(
        model="dall-e-3",
        prompt=img_generator_prompt,
        size="1792x1024",
        quality="standard",
        n=1,
    )

    image_url = response.data[0].url
    
    response_img = requests.get(image_url)
    if response_img.status_code == 200:
        output_dir = Path(settings.MEDIA_ROOT) / "thread_cover_img"
        output_dir.mkdir(parents=True, exist_ok=True)
        file_name = f"{uuid.uuid4()}.png"
        file_path = output_dir / file_name
        file_path.write_bytes(response_img.content)
        return str(Path("thread_cover_img") / file_name)

    return None

def embed_books(book_desc_list):
    headers = {
        "Authorization": f"Bearer {emb_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "input": book_desc_list,
        "model": "solar-embedding-1-large-passage",
    }
    response = requests.post(
        "https://api.upstage.ai/v1/solar/embeddings",
        headers=headers,
        json=data,
    )
    response.raise_for_status()
    return [item["embedding"] for item in response.json()["data"]]

def get_or_create_book_vectors(books):
    if CACHE_PATH.exists():
        with open(CACHE_PATH, "rb") as f:
            return pickle.load(f)

    # 전체 책 설명 필터링
    descs = [
        b.description.strip()[:2048]
        for b in books
        if b.description and isinstance(b.description, str) and b.description.strip()
    ]

    # 여러 배치로 나눠서 벡터 생성
    all_vectors = []
    for i in range(0, len(descs), BATCH_SIZE):
        batch = descs[i:i+BATCH_SIZE]
        print(f"🔄 Embedding batch {i} ~ {i+len(batch)-1}")
        vectors = embed_books(batch)
        all_vectors.extend(vectors)

    # 결과 캐시 저장
    with open(CACHE_PATH, "wb") as f:
        pickle.dump(all_vectors, f)

    return all_vectors

def recommend_similar_books(target_index, all_embeddings, top_k=6):
    sims = cosine_similarity([all_embeddings[target_index]], all_embeddings)[0]
    sim_scores = list(enumerate(sims))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    return [idx for idx, _ in sim_scores[1:top_k+1]]