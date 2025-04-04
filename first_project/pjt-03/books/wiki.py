import wikipediaapi
import requests
from openai import OpenAI

def wiki(author):
    wiki_wiki = wikipediaapi.Wikipedia('wiki/1.0 (your_@email.com)', 'ko')
    page_py = wiki_wiki.page(author)
    
    text=page_py.text
    # image_url = list(page_py.images.values())[0]
    return text

# def get_author_image(title):
#     S = requests.Session()
#     URL = "https://en.wikipedia.org/w/api.php"

#     PARAMS = {
#         "action": "query",
#         "titles": title,
#         "prop": "pageimages",
#         "format": "json",
#         "pithumbsize": 500  # 이미지 해상도 조절
#     }

#     response = S.get(url=URL, params=PARAMS)
#     data = response.json()
#     pages = data["query"]["pages"]

#     for page_id in pages:
#         if "thumbnail" in pages[page_id]:
#             return pages[page_id]["thumbnail"]["source"]
#     return None

# def get_author_image(title):
#     url = "https://en.wikipedia.org/w/api.php"
#     params = {
#         "action": "query",
#         "format": "json",
#         "titles": title,
#         "prop": "pageimages",
#         "pithumbsize": 500  # 500px 크기의 썸네일 요청
#     }

#     response = requests.get(url, params=params)
#     data = response.json()

#     pages = data.get("query", {}).get("pages", {})
    
#     for page_id, page_data in pages.items():
#         if "thumbnail" in page_data:
#             return page_data["thumbnail"]["source"]  # ✅ 이미지 URL
#     return None

def gpt(text):
    OPENAI_API_KEY= "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    user_prompt=text
    prom="당신은 구조화 되지 않은 데이터를 JSON형식으로 변환하는 AI입니다. 사용자가 작가 정보를 제공하면 작가 정보와 대표 작품 목록을 JSON 형식으로 추출하세요. 키는 'author_info'와 'author_works'로 두개만 작성하고 author_info의 value는 한줄 '헤르만 카를 헤세(독일어: Hermann Karl Hesse, 1877년 7월 2일 ~ 1962년 8웟 9일)는 독일계 스위스인이며, 시인, 소설가, 화가이다.'형식을 참고해서 작성하고, author_works의 value는 도서 5개를 '책제목1, 책제목2, 책 제목3, ...' 문자열 형태로 출력하세요."
    response = client.responses.create(
    model="gpt-4o-mini",
    input=[
        {
        "role": "system",
        "content": [
            {
            "type": "input_text",
            "text": prom
            }
        ]
        },
        {
        "role": "user",
        "content": [
            {
            "type": "input_text",
            "text": user_prompt
            }
        ]
        }
    ],
    text={"format": {"type": "json_object"}},
    temperature=1,
    max_output_tokens=256
    )
    print(response.output_text)
    return(response.output_text)

   