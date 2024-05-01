from pipeline import scrape_archetypes



if __name__ == "__main__":
    archetypes = "Dark Magician"
    scrape_archetypes(archetypes, data_path="GAN_experiments/training_magician/darkmagician", 
                      csv_path="GAN_experiments", csv_name="training_cards.csv",
                      card_types = ["monster"])