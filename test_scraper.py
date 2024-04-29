from pipeline import scrape_archetypes



if __name__ == "__main__":
    archetypes = "Dark Magician,NEos, Blue-Eyes"
    scrape_archetypes(archetypes, data_path="training_images")