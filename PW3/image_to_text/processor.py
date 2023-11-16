from transformers import BlipProcessor, BlipForConditionalGeneration


class Processor:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

    async def process(self, data, model):
        # создаём инпуты
        inputs = self.processor(data, return_tensors="pt")
        
        # генерируем описание
        out = model.generate(**inputs)

        # декодированный результат
        return self.processor.decode(out[0], skip_special_tokens=True).capitalize()
