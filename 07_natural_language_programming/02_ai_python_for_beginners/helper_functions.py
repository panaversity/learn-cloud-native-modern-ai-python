import google.generativeai as genai
from google.colab import userdata

GOOGLE_API_KEY = userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

# Define the model with system instructions
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # or "gemini-1.5-flash" for another version
    system_instruction="You are a helpful and concise python coding AI assistant. Provide clear and to-the-point responses."
)


def print_llm_response(prompt):
    """This function takes a prompt as input, sends it to Google Gemini's model, and prints the response."""
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")

        # Generate content using the model
        response = model.generate_content(prompt)
        print("_" * 100)
        print(response.text)
        print("_" * 100)
        print("\n")
    except TypeError as e:
        print("Error:", str(e))


def get_llm_response(prompt):
    """This function takes a prompt, sends it to Google Gemini's model, and returns the response as a string."""
    response = model.generate_content(prompt)
    return response.text


def get_chat_completion(prompt, history):
    """Generate a response based on chat history and the new prompt."""
    history_string = "\n\n".join(["\n".join(turn) for turn in history])
    prompt_with_history = f"{history_string}\n\n{prompt}"

    # Generate content with history
    response = model.generate_content(prompt_with_history)
    return response.text
