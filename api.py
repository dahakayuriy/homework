import requests
from googletrans import Translator
import sys

# Отримання поточного статусу війни
status_url = "https://russianwarship.rip/api/v2/war-info/status"
status_response = requests.get(status_url)
status_response.encoding = 'utf-8'
status_data = status_response.json()

if status_response.status_code == 200:
    # Переклад англійської назви статусу на українську
    english_status = status_data["data"]["alias"]

    # Використання бібліотеки googletrans
    translator = Translator()

    try:
        translation = translator.translate(english_status, dest="uk")
        ukrainian_status = translation.text
    except Exception as e:
        print(f"Error translating to Ukrainian: {str(e)}")
        ukrainian_status = "Translation error"

    # Встановлення кодування для коректного виведення українського тексту
    print(f"Current War Status (English): {english_status}")

    try:
        sys.stdout.reconfigure(encoding='utf-8')
        print(f"Current War Status (Ukrainian): {ukrainian_status}")
    except UnicodeEncodeError:
        print("Unable to display Ukrainian characters in this environment.")
else:
    print(f"Error fetching current war status: {status_data['message']}")
# Отримання останньої статистики
latest_statistics_url = "https://russianwarship.rip/api/v2/statistics/latest"
latest_statistics_response = requests.get(latest_statistics_url)
latest_statistics_data = latest_statistics_response.json()

if latest_statistics_response.status_code == 200:
    print("\nLatest War Statistics:")
    print(latest_statistics_data)
else:
    print(
        f"Error fetching latest war statistics: {latest_statistics_data['message']}")

# Отримання статистики за вказану дату (наприклад, 2022-04-14)
date_statistics_url = "https://russianwarship.rip/api/v2/statistics/2022-04-14"
date_statistics_response = requests.get(date_statistics_url)
date_statistics_data = date_statistics_response.json()

if date_statistics_response.status_code == 200:
    print(f"\nWar Statistics for 2022-04-14:")
    print(date_statistics_data)
else:
    print(
        f"Error fetching war statistics for 2022-04-14: {date_statistics_data['message']}")
