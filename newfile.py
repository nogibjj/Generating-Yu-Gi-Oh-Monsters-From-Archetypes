import requests
import json
import csv
import time
import os

# # Draws the download progress bar for images
# def draw_loader(file, total, count):
#     """
#     Draws a download progress bar.
#     Args:
#         file (str): The name of the file being downloaded.
#         total (int): Total number of files to download.
#         count (int): Number of files already downloaded.
#     """
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print('Downloading images\n')
#     print(file, end='')
#     print(' ' + str(count) + ' of ' + str(total))
#     percent = (count/total) * 100
#     print('[', end='')
#     for i in range(30):
#         if (i/30) * 100 >= percent:
#             print('-', end='')
#         else:
#             print('#', end='')
#     print(']{:.2f}%'.format(percent))

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
    request = requests.get(url)
    data_request = request.content

    # Prepares the links of the images for cards with English text
    card_info = prepare_json(data_request)
    image_quantity = len(card_info)

    # Create and open a CSV file to store card information
    with open('card_information.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "type", "desc", "atk", "def", "level", "race", "attribute"])
        writer.writeheader()

        # Write card information to CSV file
        for card in card_info:
            writer.writerow(card)

    # # For each card, fetches all images and stores them in the card_images/ directory
    # for i in range(image_quantity):
    #     id = card_info[i]["id"]
    #     link = card_info[i]["image_url"]
    #     file_name = id + '.jpg'

    #     # Draws progress bar 
    #     draw_loader(file_name, image_quantity, i+1)

    #     # Downloads the file
    #     image = requests.get(link, allow_redirects=True)
    #     open('card_images/' + file_name, 'wb').write(image.content)

    #     # Sleeps to not exceed the limit allowed by the API
    #     time.sleep(0.05)
    # print('Process Finished!')

if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
