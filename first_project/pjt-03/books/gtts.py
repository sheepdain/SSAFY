from gtts import gTTS
import os
import requests
from openai import OpenAI

def gpt(text):
    OPENAI_API_KEY= "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"
    client = OpenAI(api_key=OPENAI_API_KEY)
    user_prompt=text
    prom="당신은 도서 및 작가 데이터를 스크립트로 생성하는 AI입니다. 사용자가 작가 정보와 작품 정보를 제공하면 str형식으로로 추출하세요."
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

from gtts import gTTS

# def create_audio_file(text_file, audio_file):
#     with open(text_file, 'r', encoding='utf-8') as file:
#         text = file.read()
    
#     tts = gTTS(text=text, lang='ko')
    
#     tts.save(audio_file)
    
