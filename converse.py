import openai
import os

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_model_response(model, conversation_history):
    response = openai.ChatCompletion.create(
        model=model,
        messages=conversation_history
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    # Request user input for the task
    task1 = input("Please input the initial system propmt for model 1: ")
    requested_request = input("Please input the initial output for model 1: ")
    task2 = input("Please input the initial system propmt for model 2: ")

    # Set up the initial conversation context for both models
    model_1_name = "gpt-3.5-turbo"
    model_2_name = "gpt-3.5-turbo"

    conversation_history_model_1 = []
    conversation_history_model_2 = []

    conversation_history_model_1.append({"role": "system", "content": task1})
    conversation_history_model_1.append({"role": "user", "content": requested_request})

    conversation_history_model_2.append({"role": "system", "content": task2})

    # Converse for a specified number of turns
    num_turns = 10
    for i in range(num_turns):
        # Model 1 responds
        response_model_1 = get_model_response(model_1_name, conversation_history_model_1)
        conversation_history_model_1.append({"role": "assistant", "content": response_model_1})
        conversation_history_model_2.append({"role": "user", "content": response_model_1})

        print(f"Model 1: {response_model_1}\n\n")

        # Model 2 responds
        response_model_2 = get_model_response(model_2_name, conversation_history_model_2)
        conversation_history_model_1.append({"role": "user", "content": response_model_2})
        conversation_history_model_2.append({"role": "assistant", "content": response_model_2})

        print(f"Model 2: {response_model_2}\n\n")


if __name__ == "__main__":
    main()
