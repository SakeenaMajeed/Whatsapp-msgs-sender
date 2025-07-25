# import os
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# from dotenv import load_dotenv

# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")

# if gemini_api_key is None:
#     raise ValueError("GEMINI_API_KEY is not set")

# client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# model = OpenAIChatCompletionsModel(
#     openai_client=client,
#     model="gemini-2.0-flash"
# )

# config = RunConfig(
#     model=model,
#     model_provider=client,
#     tracing_disabled=True
# )

# Function to use in Streamlit
async def generate_message(prompt: str) -> str:
    response = await model.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content
