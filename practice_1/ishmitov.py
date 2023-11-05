from transformers import pipeline
from diffusers import DiffusionPipeline
import torch
from datetime import datetime

translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en")

while 1 > 0:
    try:
        user_text = input("Введите текст для создания картиночки, а если надоело введите \"exit\": ")
        if user_text == "exit":
            print("Досвиданья")
            break

        pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
        pipe.enable_attention_slicing()

        if not torch.cuda.is_available():
            pipe = pipe.to("mps")

        prompt = translator(user_text)[0]['translation_text']
        print(prompt)
        image = pipe(prompt).images[0]

        current_timestamp_ms = str(round(datetime.now().timestamp() * 1000))

        path = "./" + current_timestamp_ms + ".png"
        image.save(path)
        print("Картинка сохранена по пути: ", path)
    except UnicodeDecodeError:
        print("Ошибка декодирования. Введите текст, соответствующий кодировке UTF-8.")
    except Exception as ex:
        print(ex)