from scraping_functions.pipeline import scrape_archetypes, dataset_cleaner
from scraping_functions.card_sampler import build_sample
import os
import pandas as pd

if __name__ == "__main__":

    experiment_archetypes = [{"archetype" : "Dark Magician", "img_path" : "training_data_final/darkmagician_images", "csv_path" : "training_data_final", "csv_name" : "darkmagician_cards.csv"},
                                {"archetype" : "Blue-Eyes", "img_path" : "training_data_final/blueeyes_images", "csv_path" : "training_data_final", "csv_name" : "blueeyes_cards.csv"},
                                {"archetype" : "Elemental Hero", "img_path" : "training_data_final/elementalhero_images", "csv_path" : "training_data_final", "csv_name" : "elementalhero_cards.csv"},
                                {"archetype" : "All", "img_path" : "training_data_final/sampled_training_images", "csv_path" : "training_data_final", "csv_name" : "sampled_all_training_cards.csv"}]

    for archetypes in experiment_archetypes:
        # scrape the archetype and remove the bad images/records.
        archetype = archetypes["archetype"]
        img_path = archetypes["img_path"]
        csv_path = archetypes["csv_path"]
        csv_name = archetypes["csv_name"]
        scrape_archetypes(archetype, data_path=img_path, csv_path=csv_path, csv_name=csv_name)
        print("Scraping for", archetype, "completed!")
        print("Starting to clean " + archetype)
        dataset_cleaner(dataset_path = img_path, csv_path = csv_path + os.path.sep + csv_name)

        if archetypes["archetype"].lower() == "all":
            # Sample from the larger dataset, but only half of it.
            img_path = archetypes["img_path"]
            csv_path = archetypes["csv_path"] + os.path.sep + archetypes["csv_name"]
            df = pd.read_csv(csv_path)
            print("The dataset contains {} images".format(len(os.listdir(img_path))))
            print("The csv has ", df.shape)
            print("Creating sampled data")
            build_sample(img_path, csv_path, random_state=42)    
            print("Sampled data created!")
