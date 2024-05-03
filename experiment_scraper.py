from pipeline import scrape_archetypes



if __name__ == "__main__":

    experiment_archetypes = [{"archetype" : "Dark Magician", "path" : "training_data_final/darkmagician_images", "csv_path" : "training_data_final", "csv_name" : "darkmagician_cards.csv"},
                                {"archetype" : "Blue-Eyes", "path" : "training_data_final/blueeyes_images", "csv_path" : "training_data_final", "csv_name" : "blueeyes_cards.csv"},
                                {"archetype" : "Elemental Hero", "path" : "training_data_final/elementalhero_images", "csv_path" : "training_data_final", "csv_name" : "elementalhero_cards.csv"}]
    
    for archetypes in experiment_archetypes:
        scrape_archetypes(archetypes, data_path="training_images", csv_path="training_da", csv_name="training_cards.csv")