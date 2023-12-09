import openai

openai.api_key = "your_api_key_here"

messages = [ {"role": "system", "content":
              "You are intelligent assistant."}
            ]
while True:
    message = input('User: ')
    if message:
        messages.append(
                {"role": "user", "content": message},
                )
        chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
                )
        replay = chat.choices[0].message.content
        print(f"ChatGPT: {replay}")
        messages.append({"role": "assistant", "content": replay})