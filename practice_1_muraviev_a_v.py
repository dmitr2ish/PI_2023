from transformers import pipeline

if __name__ == '__main__':
    qa_pipeline = pipeline(
        "question-answering",
        model="mrm8488/bert-small-finetuned-squadv2",
        tokenizer="mrm8488/bert-small-finetuned-squadv2"
    )

    print("Программа отвечает на вопросы по указанному тексту")
    print("Пример:")
    print("======================")
    print("Текст: fish costs 7 hundred dollars")
    print("Вопрос к тексту: how much is the fish")
    print(qa_pipeline(
        {'context': "fish costs 7 hundred dollars on the market and 34 at shop",
         'question': "how much is the fish on the market"}))
    print("======================")

    user_context = input("Введите ваш текст: ")
    user_question = input("Вопрос к тексту: ")
    print(qa_pipeline(
        {'context': user_context,
         'question': user_question}))



