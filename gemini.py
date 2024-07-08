import google.generativeai as genai
def get_command(req):

    genai.configure(api_key="AIzaSyCWWtUtBdisAIiOYf2DkRatQb6VyHSWLcQ")
    # Create the model
    # See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
    generation_config = {
      "temperature": 1,
      "top_p": 0.95,
      "top_k": 64,
      "max_output_tokens": 8192,
      "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
      model_name="gemini-1.5-flash",
      generation_config=generation_config,
      safety_settings = [
          {
              "category": "HARM_CATEGORY_HARASSMENT",
              "threshold": "BLOCK_NONE",
          },
          {
              "category": "HARM_CATEGORY_HATE_SPEECH",
              "threshold": "BLOCK_NONE",
          },
          {
              "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
              "threshold": "BLOCK_NONE",
          },
          {
              "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
              "threshold": "BLOCK_NONE",
          },
      ]
      # See https://ai.google.dev/gemini-api/docs/safety-settings
    )

    chat_session = model.start_chat(
      history=[
      ]
    )

    response = chat_session.send_message(f"Give me only the command i would type in command promt to {req} and not any additon information")
    return response[3:-3]