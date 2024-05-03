from lib.scraper_scripts.card_image_scraper import *
from lib.scraper_scripts.card_info_extractor import *
import requests
import json
import csv
import time
import os
import re
import pandas as pd
import cv2


def process_archetype_input(archetypes):
    """Processes the input of archetypes.
    Args:
        archetypes: string containing the names
    Returns:
        archetype_set: set containing
        the names of the archetypes
    """
    archetype_list = archetypes.split(",")
    archetype_list = [archetype.strip() for archetype in archetype_list]
    archetype_list = [archetype.lower() for archetype in archetype_list]
    archetype_set = set(archetype_list)
    return archetype_set


def search_archetype(card_from_request, archetype_set):
    """Returns True if the card contains the archetype in
    its name or description.
    Args:
        card_from_request: dictionary containing card information
        archetype_set: set containing the names of the archetypes
    Returns:
        bool: True if the card contains the archetype in
        its name or description, False otherwise
    """
    for archetype in archetype_set:
        if archetype in card_from_request["name"].lower():
            return True
        elif archetype in card_from_request["desc"].lower():
            return True
    return False


def extract_info(json_data, archetypes):
    """Extracts the card information from the JSON data.
    Args:
        json_data: JSON data containing card information.
        archetypes: list of archetypes
    Returns:
        list: A list of dictionaries containing card information
        for the given archetypes.
    """
    card_info = []
    for card in json_data:
        if "en" in card["desc"] and (search_archetype(card, archetypes) or "all" in archetypes):
            card_dict = {
                "id": card["id"],
                "name": card["name"],
                "type": card["type"],
                "desc": card["desc"],
                "atk": card.get("atk", 0),  # Check if 'atk' exists, if not, set to 0
                "def": card.get("def", 0),  # Check if 'def' exists, if not, set to 0
                "level": card.get(
                    "level", 0
                ),  # Check if 'level' exists, if not, set to 0
                "race": card["race"],
                "attribute": card.get(
                    "attribute", "Unknown"
                ),  # Check if 'attribute' exists, if not, set to 'Unknown'
                "archetype": card.get("archetype", "Unknown"),
            }
            image_urls = [url["image_url_cropped"] for url in card.get("card_images", "")]
            urls_count = len(image_urls)
            if urls_count == 0:
                card_dict["image_url"] = ""
                card_info.append(card_dict)
            else:
                for i in range(urls_count):
                    copy_card_dict = card_dict.copy()
                    copy_card_dict["image_url"] = image_urls[i]
                    card_info.append(copy_card_dict)
    return card_info


def download_images(card_info, data_path="training_images", card_types = ["spell", "trap", "monster", "token"]):
    """Downloads the images of the cards to the data path
    and adds the path to the card information.
    Args:
        card_info: list of dictionaries containing card information
        data_path: path to store the images
    Returns:
        None
    """

    image_quantity = len(card_info)
    for i in range(image_quantity):
        id = str(card_info[i]["id"])
        link = card_info[i]["image_url"]
        type_of_card = set(card_info[i]["type"].lower().split(" "))
        valid_type=False

        for c_type in type_of_card:
            if c_type in card_types:
                valid_type=True

        if valid_type:
            try:
                name = re.findall("([0-9]+\..*)", link)[0]
                filename = data_path + os.path.sep + name
                draw_loader(name, image_quantity, i + 1)
                image = requests.get(link, allow_redirects=True)
                open(filename, "wb").write(image.content)
                time.sleep(0.05)
            except IndexError:
                print("Error with link:", link)
                pass
            card_info[i]["image_path"] = filename
            card_info[i]["file_name"] = filename.split("/")[-1]
        else:
            pass
    print("Process Finished!")


def scrape_archetypes(archetypes, data_path="training_images", csv_path="training_images", 
                      csv_name="training_cards.csv", card_types = ["spell", "trap", "monster", "token"]):
    """
    archetypes: string containing the names
    Examples below
    ex1: "Blue-Eyes White Dragon, Dark Magician"
    ex2: "Red-Eyes Black Dragon"
    """

    if not os.path.exists(data_path):
        os.makedirs(data_path)
    
    archetype_set = process_archetype_input(archetypes)
    card_types = set(card_types)

    URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

    try:
        request = requests.get(URL)
        request.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data_request = request.content
        data = json.loads(data_request)["data"]

        # Extracting the card information for the given archetypes
        card_info = extract_info(data, archetype_set)
        download_images(card_info, data_path, card_types)

        with open(csv_path + os.path.sep + csv_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=list(card_info[0].keys()))
            writer.writeheader()
    
            for card in card_info:
                # Skip Skill Cards
                # if card["type"] == "Skill Card":
                #     continue
                for type in set(card["type"].lower().split(" ")):
                    if type in card_types:
                        writer.writerow(card)

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

def dataset_cleaner(dataset_path, csv_path):
    """
    Removes images and records that cannot be read by cv2
    """
    df = pd.read_csv(csv_path)
    erased_images_list = []
    print("The dataset contains {} images".format(len(os.listdir(dataset_path))))
    print("The csv has ", df.shape)
    for image in os.listdir(dataset_path):
        img = cv2.imread(os.path.join(dataset_path, image))
        if img is None:
            print("Removed image : " + image)
            os.remove(os.path.join(dataset_path, image))
            erased_images_list.append(image)

    df = df[~df['file_name'].isin(erased_images_list)].reset_index(drop=True)
    df.to_csv(csv_path, index=False)
    print("The dataset now contains {} images".format(len(os.listdir(dataset_path))))
    print("The csv now has ", df.shape)
    return 

if __name__ == "__main__":
    os.system("cls" if os.name == "nt" else "clear")
    scrape_archetypes("Blue-Eyes White Dragon, Dark Magician, Red-Eyes Black Dragon")
    print("Done!")
    for img in os.listdir("training_images"):
        os.remove(os.path.join("training_images", img))
