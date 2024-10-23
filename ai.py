import os
import requests
import json
from dotenv import load_dotenv
from payload import pay

load_dotenv()

# Получение ключа API Voiceflow и Project ID
VOICEFLOW_API_KEY = os.getenv('VOICEFLOW_API_KEY')
PROJECT_ID = os.getenv('PROJECT_ID')

# Основная логика
def interact_stream(user_id, data):
    url = f"https://general-runtime.voiceflow.com/v2/project/{PROJECT_ID}/user/{user_id}/interact/stream"

    headers = {
        'Accept': 'text/event-stream',
        'Authorization': VOICEFLOW_API_KEY,
        'Content-Type': 'application/json'
    }

    # Отправляем POST запрос с параметрами и включаем поток (stream=True)
    response = requests.post(url, headers=headers, json=data, stream=True)

    if response.status_code == 200:
        print("Connected to stream, receiving data...\n")
        for line in response.iter_lines():
            if line:
                # Декодируем строку
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith("data:"):
                    # Извлекаем полезные данные после 'data:'
                    try:
                        parsed_data = json.loads(decoded_line[6:])
                        process_stream_data(parsed_data)
                    except json.JSONDecodeError:
                        print(f"Unable to parse: {decoded_line}")
    else:
        print(f"Error: {response.status_code}")


def process_stream_data(data):
    # Извлекаем текстовые сообщения и выводим в структурированном виде
    if "payload" in data and "slate" in data["payload"]:
        slate_content = data["payload"]["slate"]["content"]
        print("---- Сообщение от Voiceflow ----")
        for block in slate_content:
            for child in block['children']:
                print(child['text'])
        print("-------------------------------\n")

# Данные для взаимодействия
data = {
    "action": {
        "type": "launch"
    }
}

data_text = {
    "action": {
        "type": "text",
        'payload': f'{pay}'
    }
}

# Использование
def main():
    user_id = "your_user_id_here"  # Замените на реальный user_id
    interact_stream(user_id, data)
    interact_stream(user_id, data_text)

if __name__ == '__main__':
    main()
