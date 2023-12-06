import openai

def ask_openai(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
            engine = "text-davinci-003",
            prompt = prompt,
            max_tokens = 1000,
    )

    return response.choices[0].text.strip()

def main():
    api_key = "Your_api_key_here"
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            print('Goodbye.')
            break
        prompt = f"You: {user_input}\nOpenAI:"
        response = ask_openai(prompt, api_key)
        print(response)

if __name__ == "__main__":
    main()