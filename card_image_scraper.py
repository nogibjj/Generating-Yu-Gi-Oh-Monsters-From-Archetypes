import requests
import json 
import time
import os

# Draws the download progress bar for images
def draw_loader(file, total, count):
    """
    Draws a download progress bar.
    Args:
        file (str): The name of the file being downloaded.
        total (int): Total number of files to download.
        count (int): Number of files already downloaded.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Downloading images\n')
    print(file, end='')
    print(' ' + str(count) + ' of ' + str(total))
    percent = (count/total) * 100
    print('[', end='')
    for i in range(30):
        if (i/30) * 100 >= percent:
            print('-', end='')
        else:
            print('#', end='')
    print(']{:.2f}%'.format(percent))

# Receives the JSON and returns a list with the IDs and the links to the images for cards with English text
def prepare_json(data_request):
    """
    Prepares the list of IDs and image links for cards with English text.
    Args:
        data_request (str): JSON data containing card information.
    Returns:
        list: A list of lists containing ID and image link pairs for cards with English text.
    """
    data = json.loads(data_request)['data']
    link_images = []
    for i in range(len(data)):
        if 'en' in data[i]['desc']:
            for j in range(len(data[i]['card_images'])):
                id = data[i]['card_images'][j]['id']
                link = data[i]['card_images'][j]['image_url']
                link_images.append([str(id), link])
    return link_images

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
    link_images = prepare_json(data_request)
    image_quantity = len(link_images)

    # For each card, fetches all images and stores them in the card_images/ directory
    for i in range(image_quantity):
        id = link_images[i][0]
        link = link_images[i][1]
        file_name = id + '.jpg'

        # Draws progress bar 
        draw_loader(file_name, image_quantity, i+1)

        # Downloads the file
        image = requests.get(link, allow_redirects=True)
        open('card_images/' + file_name, 'wb').write(image.content)

        # Sleeps to not exceed the limit allowed by the API
        time.sleep(0.05)
    print('Process Finished!')


if __name__ == '__main__':
    os.system('cls' if os.name == 'nt' else 'clear')
    main()