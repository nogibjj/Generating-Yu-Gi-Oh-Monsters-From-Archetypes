import requests
import json
import csv
import time
import os

def prepare_json(data_request):
    """
    Prepares the list of IDs and image links for cards with English text.
    Args:
        data_request (str): JSON data containing card information.
    Returns:
        list: A list of dictionaries containing card information.
    """
    data = json.loads(data_request)['data']
    card_info = []
    for card in data:
        if 'en' in card['desc']:
            card_dict = {
                "id": card['id'],
                "name": card['name'],
                "type": card['type'],
                "desc": card['desc'],
                "atk": card.get('atk', 0),  # Check if 'atk' exists, if not, set to 0
                "def": card.get('def', 0),  # Check if 'def' exists, if not, set to 0
                "level": card.get('level', 0),  # Check if 'level' exists, if not, set to 0
                "race": card['race'],
                "attribute": card.get('attribute', 'Unknown')  # Check if 'attribute' exists, if not, set to 'Unknown'
            }
            card_info.append(card_dict)
    return card_info

def main():
    """
    Downloads images of Yu-Gi-Oh! cards with English text.
    Fetches card data from the API, prepares image links, downloads images, and stores them.
    """
    # Link to the API for around 11,000 cards
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    
    try:
        request = requests.get(url)
        request.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data_request = request.content

        # Prepares the links of the images for cards with English text
        card_info = prepare_json(data_request)
        image_quantity = len(card_info)

        # Create and open a CSV file to store card information
        with open('card_database.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "name", "type", "desc", "atk", "def", "level", "race", "attribute"])
            writer.writeheader()

            # Write card information to CSV file
            for card in card_info:
                writer.writerow(card)

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
