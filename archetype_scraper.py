"""Script that scrapes the archetypes for the study"""

from scraping_functions.pipeline import scrape_archetypes

if __name__ == "__main__":
    archetypes_list = [["Dark Magician", "GAN_experiments/training_data/darkmagician", "GAN_experiments/training_data", "training_cards_magician.csv"],
                       ["Elemental Hero", "GAN_experiments/training_data/elementalhero", "GAN_experiments/training_data", "training_cards_elemental_hero.csv"],
                        ["Blue-Eyes", "GAN_experiments/training_data/blueeyes", "GAN_experiments/training_data", "training_cards_blue_eyes.csv"]]
   
    for arch in archetypes_list:
        scrape_archetypes(arch[0], data_path=arch[1], csv_path=arch[2], csv_name=arch[3])
        print("Finished scraping", arch[0])