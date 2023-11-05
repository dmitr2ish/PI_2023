from transformers import pipeline

translator = pipeline("translation_ru_to_en", "Helsinki-NLP/opus-mt-ru-en" )

while 1>0:
    try:
        user_text = input("Введите текст для перевода на английский, а если надоело введите \"exit\": ")
        if user_text == "exit":
            print("Досвиданья")
            break
        print(translator(user_text)[0]['translation_text'])
    except Exception as ex:
        print(format("Найдена ошибочка {}, ничего страшного продолжайте работу", ex))
