from pipeline import scrape_archetypes



if __name__ == "__main__":
    archetypes_list = [["Magician", "GAN_experiments/training_magician/darkmagician", "GAN_experiments", "training_cards_magician.csv"],
                       ["elemental hero", "GAN_experiments/training_magician/elementalhero", "GAN_experiments", "training_cards_elemental_hero.csv"],
                        ["Blue-Eyes", "GAN_experiments/training_magician/blueeyes", "GAN_experiments", "training_cards_blue_eyes.csv"]]

    archetypes = "Magician"
    scrape_archetypes(archetypes, data_path="GAN_experiments/training_magician/darkmagician", 
                      csv_path="GAN_experiments", csv_name="training_cards.csv")
                    #   card_types = ["monster"])
                    
    for arch in archetypes_list:
        scrape_archetypes(arch[0], data_path=arch[1], csv_path=arch[2], csv_name=arch[3])
        print("Finished scraping", arch[0])