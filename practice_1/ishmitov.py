# from transformers import pipeline
#
# translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en" )
#
# while 1>0:
#     try:
#         user_text = input("Введите текст для перевода на английский, а если надоело введите \"exit\": ")
#         if user_text == "exit":
#             print("Досвиданья")
#             break
#         print(translator(user_text)[0]['translation_text'])
#     except Exception as ex:
#         print(format("Найдена ошибочка {}, ничего страшного продолжайте работу", ex))
from diffusers import DiffusionPipeline
import torch
from datetime import datetime

pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.enable_attention_slicing()
if not torch.cuda.is_available():
    pipe = pipe.to("mps")
prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]
current_timestamp_ms = str(round(datetime.now().timestamp() * 1000))
print(current_timestamp_ms)
path = "./practice_1/picture_out/" + current_timestamp_ms + ".png"
image.save(path)
print("Картинка сохранена по пути: ", path)