import requests
from apikey import MYAPIKEY
import os
import PIL.Image as Image


def get_stable_diffusion_image(
    prompt,
    output_format,
    MYAPIKEY,
    file_name,
    target_name,
    target_folder_path="streamlit_images",
) -> bytes:

    with open(file_name, "rb") as f:
        image_bytes = f.read()

    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={"authorization": f"Bearer {MYAPIKEY}", "accept": "image/*"},
        files={"image": image_bytes},
        data={
            "prompt": f"{prompt}",
            "output_format": f"{str(output_format)}",
            "mode": "image-to-image",
            "strength": 0.7,
            # "image": Image.open(file_name),
        },
    )

    if response.status_code == 200:
        with open(
            os.path.join(target_folder_path, f"{target_name}.{output_format}"), "wb"
        ) as file:
            file.write(response.content)
    else:
        raise Exception(str(response.json()))


if __name__ == "__main__":
    get_stable_diffusion_image(
        "Make a Yu-Gi-Oh Card with a dark magician",
        "png",
        MYAPIKEY,
        "training_images\89943723-2.jpeg",
        "mysde7",
    )
