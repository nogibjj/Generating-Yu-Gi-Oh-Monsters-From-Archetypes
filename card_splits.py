"""Helper functions for splitting during the pipeline"""
from sklearn.model_selection import train_test_split
import pandas as pd
from scraping_functions.card_sampler import classifier_type 
import os
from scraping_functions.pipeline import dataset_cleaner

def card_set_split(csv_path, img_path, class_name,source_folder):
    """Splits the data into training and testing sets.
        Args:
            class_name (str): The name of the class.
            csv_path (str): The path to the csv file.
    """
    df = pd.read_csv(csv_path)
    df["simplified_type"] = df["type"].apply(classifier_type)

    # Split the data into training and testing sets
    train, test = train_test_split(df, test_size=0.2, random_state=42, stratify=df["simplified_type"])
    print("train has " + str(train.shape[0]) + " rows")
    print("test has " + str(test.shape[0]) + " rows")

    new_class_name = class_name + "_data"

    # create the paths
    train_path = source_folder + os.path.sep + new_class_name + os.path.sep + "train"
    test_path = source_folder + os.path.sep + new_class_name + os.path.sep + "test"

    if not os.path.exists(train_path):
        os.makedirs(train_path)

    if not os.path.exists(test_path):
        os.makedirs(test_path)

    # Save the training and testing sets
    
    train.to_csv(train_path + os.path.sep + "metadata.csv", index=False)
    test.to_csv(test_path + os.path.sep + "metadata.csv", index=False)
    
    # copy images in those csvs to other folders

    train_images = set(train["file_name"].values)
    test_images = set(test["file_name"].values)

    for img in os.listdir(img_path):

        if img in train_images:
            os.rename(os.path.join(img_path, img), os.path.join(train_path, img))
        elif img in test_images:
            os.rename(os.path.join(img_path, img), os.path.join(test_path, img))

    print("Data split successfully!")

    return

if __name__ == "__main__":

    csv_path = "training_data_final/all_training_cards.csv"
    img_path = "training_data_final/training_images"
    class_name = "all"
    source_folder = "training_data_final"
    
    dataset_cleaner(img_path, csv_path)

    card_set_split(csv_path, img_path, class_name,source_folder)

    for arch in ["darkmagician", "blueeyes", "elementalhero"]:
        csv_path = "training_data_final/" + arch + "_cards.csv"
        img_path = "training_data_final/" + arch + "_images"
        class_name = arch
        source_folder = "training_data_final"
        dataset_cleaner(img_path, csv_path)
        card_set_split(csv_path, img_path, class_name,source_folder)

print("Done!")