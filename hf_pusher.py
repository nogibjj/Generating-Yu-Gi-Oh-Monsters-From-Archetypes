"""Script to push to HuggingFace, written by Shin Jiwon, pushed by Eric."""

from datasets import load_dataset


for a_dataset in ["darkmagician", "blueeyes", "elementalhero", "all"]:
    # imagefolder as a name cleared out the errors for us
    test_dataset = load_dataset("imagefolder", data_dir=f"training_data_final/{a_dataset}_data")

    # modify with your directory
    test_dataset.push_to_hub(f"steamcyclone/{a_dataset}_data", private=True)

# # imagefolder as a name cleared out the errors for us
# test_dataset = load_dataset("imagefolder", data_dir="training_data_final/darkmagician_data")

# # modify with your directory
# test_dataset.push_to_hub("steamcyclone/darkmagician", private=True)