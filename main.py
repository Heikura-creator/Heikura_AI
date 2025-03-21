import ollama

def ask(question):

    response = ollama.chat(
        model="wizardlm-uncensored:latest",
        messages=[
            {"role": "user", "content": question},
        ],
    )

    return response

while True:
    question = input("Input question: ")

    #close program if the input length is less than 1
    if len(question) <= 1:
        break

    answer = ask(question)

    print(answer["message"]["content"])

