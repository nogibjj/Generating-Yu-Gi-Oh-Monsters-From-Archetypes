from pipeline import scrape_archetypes, dataset_cleaner
import os

if __name__ == "__main__":

    experiment_archetypes = [{"archetype" : "Dark Magician", "img_path" : "training_data_final/darkmagician_images", "csv_path" : "training_data_final", "csv_name" : "darkmagician_cards.csv"},
                                {"archetype" : "Blue-Eyes", "img_path" : "training_data_final/blueeyes_images", "csv_path" : "training_data_final", "csv_name" : "blueeyes_cards.csv"},
                                {"archetype" : "Elemental Hero", "img_path" : "training_data_final/elementalhero_images", "csv_path" : "training_data_final", "csv_name" : "elementalhero_cards.csv"}]

    for archetypes in experiment_archetypes:
        scrape_archetypes(archetypes["archetype"], data_path=archetypes["img_path"], csv_path=archetypes["csv_path"], csv_name=archetypes["csv_name"])
        print("Scraping for", archetypes["archetype"], "completed!")
        print("Starting to clean " + archetypes["archetype"])
        dataset_cleaner(dataset_path = archetypes["img_path"], csv_path = archetypes["csv_path"] + os.path.sep + archetypes["csv_name"])
