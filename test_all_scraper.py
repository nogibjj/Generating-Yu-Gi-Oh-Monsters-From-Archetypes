from pipeline import scrape_archetypes



if __name__ == "__main__":
    archetypes = "All"
    scrape_archetypes(archetypes, data_path="training_data_final/training_images", csv_path="training_data_final", csv_name="all_training_cards.csv")