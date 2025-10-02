from model_config import llm, trim_to_sentence, MAX_TOKENS

print("CarrieGPT 💄 — type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "exit", "quit"]:
        print("Carrie: Bye honey, talk soon! And remember — heartbreak is just fashion waiting to happen. 💋")
        break
    prompt = f"User: {user_input}\nCarrie:"
    response = llm.invoke(prompt).strip()
    final_response = trim_to_sentence(response, MAX_TOKENS)
    print(f"Carrie: {final_response}")