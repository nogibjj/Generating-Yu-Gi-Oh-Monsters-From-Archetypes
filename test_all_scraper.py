from pipeline import scrape_archetypes, dataset_cleaner
import os


if __name__ == "__main__":
    archetypes = "All"
    scrape_archetypes(archetypes, data_path="training_data_final/training_images", csv_path="training_data_final", csv_name="all_training_cards.csv")
    print("Scraping for", archetypes, "completed!")
    print("Starting to clean datasets of bad images")
    dataset_cleaner(dataset_path = "training_data_final/training_images", csv_path = "training_data_final" + os.path.sep + "all_training_cards.csv")