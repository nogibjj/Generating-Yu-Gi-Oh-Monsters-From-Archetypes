import os
import shutil

def replicate_data(data_folder, target_folder):
    """
    Replicates the data in the data_folder to the target_folder.
    :param data_folder: The folder containing the data to be replicated
    :param target_folder: The folder to which the data will be replicated
    :return: None
    """
    for img in os.listdir(data_folder):
        # copy the image
        shutil.copy(os.path.join(data_folder, img), os.path.join(target_folder, img))
    print("Data replicated successfully!")
    return

def prepare_structure(folder):

    for subfolder in os.listdir(folder):

        if not os.path.exists(folder + os.path.sep + subfolder + os.path.sep + "imgs"):
            os.makedirs(folder + os.path.sep + subfolder + os.path.sep + "imgs")

        for img in os.listdir(folder + os.path.sep + subfolder):
            if img != "imgs":
                shutil.copy(folder + os.path.sep + subfolder + os.path.sep + img, folder + os.path.sep + subfolder + os.path.sep + "imgs" + os.path.sep + img)
                os.remove(folder + os.path.sep + subfolder + os.path.sep + img)

    return

if __name__ == "__main__":
    # data_folder = "training_data_final/all_data"
    # target_folder = "training_data_final/all_data_replicated"
    
    # replicate_data(data_folder, target_folder)

    folders = ["../training_data_final/blueeyes_data", "../training_data_final/darkmagician_data", "../training_data_final/elementalhero_data"]

    for folder in folders:

        # replicate_data(folder + "/train", folder + "/train_replicated")
        # replicate_data(folder + "/test", folder + "/test_replicated")

        try:
            shutil.rmtree(folder.split("/")[-1])
            shutil.copytree(folder, folder.split("/")[-1])
        except:
            shutil.copytree(folder, folder.split("/")[-1])

        prepare_structure(folder.split("/")[-1])

    # shutil.copytree("../training_data_final/all_data", "all_data")
    # prepare_structure("all_data")