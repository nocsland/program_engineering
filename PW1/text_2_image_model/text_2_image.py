"""
Постановка задачи описана тут: text_2_image_model/README.md

Необходимые зависимости: transformers, sentencepiece, diffusers
Установка: pip install transformers sentencepiece diffusers
"""

from abc import ABC, abstractmethod

import torch
from diffusers import StableDiffusionPipeline


class BaseImageCreator(ABC):

    @abstractmethod
    def create_image(self):
        pass

    @abstractmethod
    def save_image_to_path(self):
        pass

class ImageCreator(BaseImageCreator):
    def __init__(self, pipe):
        self.pipe = pipe

    def create_image(self, prompt):
        return self.pipe(prompt).images[0]

    def save_image_to_path(self, image, file_name):
        # сохраняем полученное изображение в папку с проектом
        image.save(file_name)


if __name__ == "__main__":
    print("This is an application for creating an image from text\n")

    model = "runwayml/stable-diffusion-v1-5"

    prompt = input("Enter prompt: ")
    file_name = input("Enter file name: ")

    pipe = StableDiffusionPipeline.from_pretrained(model, torch_dtype=torch.float32)
    pipe = pipe.to("cpu")
    
    creator = ImageCreator(pipe)
    image = creator.create_image(prompt)
    creator.save_image_to_path(image, file_name)
