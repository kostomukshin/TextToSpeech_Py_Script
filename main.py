import json
import os
import time
import requests

from dotenv import load_dotenv
load_dotenv()

def text_to_speech(text="Hello friend!"):
    headers = {"Authorization": f"Bearer {os.getenv('API_KEY')}"}
    url = 'https://api.edenai.run/v2/audio/text_to_speech'

    payload = {
        'providers': 'openai',
        'language': 'en',
        'option': 'FEMALE',
        'openai': 'en_shimmer',
        'text': f'{text}'
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    #with open(f'{unx_time}.json', 'w') as file:
     #   json.dump(result, file, indent=4, ensure_ascii=False)

    audio_url = result.get('openai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'{unx_time}.wav', 'wb') as file:
        file.write(r.content)
def main():
    text_to_speech(text = 'Listen at you, now." Luster said. "Aint you something, thirty three years old, going on that way. After I done went all the way to town to buy you that cake. Hush up that moaning. Aint you going to help me find that quarter so I can go to the show tonight.')

if __name__ == "__main__":
    main()
