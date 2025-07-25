# # # # from dotenv import load_dotenv
# # # # import os
# # # # from agents import Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
# # # # load_dotenv()

# # # # openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# # # # if not openrouter_api_key:
# # # #     raise ValueError(" OPENROUTER is not set. Please ensure it is defined in your .env file.")

# # # # external_client = AsyncOpenAI(
# # # #     api_key= openrouter_api_key,
# # # #     base_url="https://openrouter.ai/api/v1",
# # # # )

# # # # model = OpenAIChatCompletionsModel(
# # # #     model="deepseek/deepseek-v3-base:free",
# # # #     openai_client=external_client
# # # # )

# # # # config = RunConfig(
# # # #     model=model,
# # # #     model_provider=external_client,
# # # #     tracing_disabled=True
# # # # )

# # # # agent = Agent(
# # # #     name = "writer Agent",
# # # #     instructions="You are a writer agent, Generate stories, poems, essay etc"
# # # # )
# # # # response = Runner.run_sync(
# # # #     agent,
# # # #     input = "write an essay on Quaid-e-Azam Muhammad Ali Jinnah ",
# # # #     run_config= config
# # # # )

# # # # print(response)

# # # # import os
# # # # import sys
# # # # from dotenv import load_dotenv

# # # # # 👉 OpenRouter Client Setup
# # # # from openai import AsyncOpenAI
# # # # from agents import OpenAIChatCompletionsModel, RunConfig

# # # # # 📦 Load API key from .env
# # # # load_dotenv()
# # # # openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# # # # if not openrouter_api_key:
# # # #     raise ValueError("❌ OPENROUTER_API_KEY is not set in your .env file!")

# # # # external_client = AsyncOpenAI(
# # # #     api_key=openrouter_api_key,
# # # #     base_url="https://openrouter.ai/api/v1"
# # # # )

# # # # model = OpenAIChatCompletionsModel(
# # # #     model="deepseek/deepseek-v3-base:free",
# # # #     openai_client=external_client
# # # # )

# # # # config = RunConfig(
# # # #     model=model,
# # # #     model_provider=external_client,
# # # #     tracing_disabled=True
# # # # )

# # # # # -------------------- Poet Agent --------------------
# # # # class PoetAgent:
# # # #     def run(self):
# # # #         print("📝 Enter your 2-stanza poem (press Enter twice to finish):")
# # # #         poem = ""
# # # #         while True:
# # # #             line = input()
# # # #             if line.strip() == "":
# # # #                 break
# # # #             poem += line + "\n"
# # # #         return poem.strip()

# # # # # -------------------- Triage Agent --------------------
# # # # class TriageAgent:
# # # #     def run(self, poem):
# # # #         poem = poem.lower()
# # # #         if any(word in poem for word in ['sad', 'heart', 'feeling', 'alone', 'yaad', 'tanha']):
# # # #             return "lyric"
# # # #         elif any(word in poem for word in ['once', 'king', 'hero', 'journey', 'war', 'fight']):
# # # #             return "narrative"
# # # #         elif any(word in poem for word in ['act', 'stage', 'dialogue', 'audience', 'character']):
# # # #             return "dramatic"
# # # #         else:
# # # #             return "lyric"  # default fallback

# # # # # -------------------- Lyric Analyst --------------------
# # # # class LyricAnalyst:
# # # #     def run(self, poem):
# # # #         return (
# # # #             "📖 Lyric Poetry Analysis:\n"
# # # #             "Yeh nazm jazbaat aur dil ke ehsaasat ka izhar hai. "
# # # #             "Poet ne apne ander ke dard, khushi ya yaadon ko share kiya hai. "
# # # #             "Koi kahani ya scene nahi, sirf feelings ka izhar hai."
# # # #         )

# # # # # -------------------- Narrative Analyst --------------------
# # # # class NarrativeAnalyst:
# # # #     def run(self, poem):
# # # #         return (
# # # #             "📖 Narrative Poetry Analysis:\n"
# # # #             "Is nazm mein kahani ka pehlu hai, jaise kisi shakhs ke safar, jang, ya waqeya ka zikr. "
# # # #             "Characters aur events ko rhyme ya rhythm mein bayan kiya gaya hai."
# # # #         )

# # # # # -------------------- Dramatic Analyst --------------------
# # # # class DramaticAnalyst:
# # # #     def run(self, poem):
# # # #         return (
# # # #             "🎭 Dramatic Poetry Analysis:\n"
# # # #             "Yeh poem stage performance ke liye likhi gayi lagti hai. "
# # # #             "Ek character apne thoughts audience ko bayan karta hai. Monologue style nazar aata hai."
# # # #         )

# # # # # -------------------- Parent Agent --------------------
# # # # class ParentAgent:
# # # #     def __init__(self):
# # # #         self.poet = PoetAgent()
# # # #         self.triage = TriageAgent()
# # # #         self.lyric = LyricAnalyst()
# # # #         self.narrative = NarrativeAnalyst()
# # # #         self.dramatic = DramaticAnalyst()

# # # #     def run(self):
# # # #         poem = self.poet.run()
# # # #         category = self.triage.run(poem)

# # # #         if category == "lyric":
# # # #             return self.lyric.run(poem)
# # # #         elif category == "narrative":
# # # #             return self.narrative.run(poem)
# # # #         elif category == "dramatic":
# # # #             return self.dramatic.run(poem)
# # # #         else:
# # # #             return "❌ Poetry type not recognized."

# # # # # -------------------- Run App --------------------
# # # # if __name__ == "__main__":
# # # #     agent = ParentAgent()
# # # #     result = agent.run()
# # # #     print("\n📘 Final Analysis:\n")
# # # #     print(result)


# # # # import os
# # # # from dotenv import load_dotenv

# # # # # OpenRouter Setup
# # # # from openai import AsyncOpenAI
# # # # from agents import OpenAIChatCompletionsModel, RunConfig

# # # # # 📌 Load API Key from .env
# # # # load_dotenv()
# # # # openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# # # # if not openrouter_api_key:
# # # #     raise ValueError("❌ OPENROUTER_API_KEY missing in .env")

# # # # # External Client Setup
# # # # external_client = AsyncOpenAI(
# # # #     api_key=openrouter_api_key,
# # # #     base_url="https://openrouter.ai/api/v1"
# # # # )

# # # # model = OpenAIChatCompletionsModel(
# # # #     model="deepseek/deepseek-v3-base:free",
# # # #     openai_client=external_client
# # # # )

# # # # config = RunConfig(
# # # #     model=model,
# # # #     model_provider=external_client,
# # # #     tracing_disabled=True
# # # # )

# # # # # ------------------ Poet Agent ------------------
# # # # class PoetAgent:
# # # #     def run(self):
# # # #         print("📝 Enter your 2-stanza poem (press Enter twice to submit):")
# # # #         poem = ""
# # # #         while True:
# # # #             line = input()
# # # #             if line.strip() == "":
# # # #                 break
# # # #             poem += line + "\n"
# # # #         return poem.strip()

# # # # # ------------------ Triage Agent ------------------
# # # # class TriageAgent:
# # # #     def run(self, poem):
# # # #         lower_poem = poem.lower()
# # # #         if any(word in lower_poem for word in ['feeling', 'love', 'heart', 'sad', 'joy', 'alone']):
# # # #             return "lyric"
# # # #         elif any(word in lower_poem for word in ['once', 'there was', 'king', 'story', 'river', 'hero']):
# # # #             return "narrative"
# # # #         elif any(word in lower_poem for word in ['stage', 'dialogue', 'act', 'audience', 'character']):
# # # #             return "dramatic"
# # # #         else:
# # # #             return "lyric"  # fallback

# # # # # ------------------ Lyric Analyst ------------------
# # # # class LyricAnalyst:
# # # #     def run(self, poem):
# # # #         return f"""🔍 Analyzing your poem...

# # # # Lyric Poetry - This poem expresses personal feelings and emotions.
# # # # The poet feels despair and sadness as light fades.
# # # # It reflects a personal loss or end of a positive phase.
# # # # The poem uses metaphor ("sun...light") and imagery ("heavy...night").
# # # # The setting sun mirrors the fading hope within the poet's heart.
# # # # It symbolizes the onset of a dark period filled with sorrow.
# # # # The "night" represents the heavy burden of grief.

# # # # 🧠 Last agent used: Lyric Poetry Analyst

# # # # 📜 Your Poem:
# # # # {poem}
# # # # """

# # # # # ------------------ Narrative Analyst ------------------
# # # # class NarrativeAnalyst:
# # # #     def run(self, poem):
# # # #         return f"""📖 Analyzing your poem...

# # # # Narrative Poetry - This poem tells a story.
# # # # It involves characters and a clear sequence of events.
# # # # The poet narrates a journey, a conflict, or a moment in time.
# # # # Words like "once", "journey", or "battle" indicate storytelling form.
# # # # There is a clear beginning, middle, and possible ending.

# # # # 🧠 Last agent used: Narrative Poetry Analyst

# # # # 📜 Your Poem:
# # # # {poem}
# # # # """

# # # # # ------------------ Dramatic Analyst ------------------
# # # # class DramaticAnalyst:
# # # #     def run(self, poem):
# # # #         return f"""🎭 Analyzing your poem...

# # # # Dramatic Poetry - This poem is written as if for performance.
# # # # The speaker seems to be talking to an audience.
# # # # Lines may be in dialogue form or monologue.
# # # # It explores inner thoughts through spoken drama.

# # # # 🧠 Last agent used: Dramatic Poetry Analyst

# # # # 📜 Your Poem:
# # # # {poem}
# # # # """

# # # # # ------------------ Parent Agent (Triage + Route) ------------------
# # # # class ParentAgent:
# # # #     def __init__(self):
# # # #         self.poet = PoetAgent()
# # # #         self.triage = TriageAgent()
# # # #         self.lyric = LyricAnalyst()
# # # #         self.narrative = NarrativeAnalyst()
# # # #         self.dramatic = DramaticAnalyst()

# # # #     def run(self):
# # # #         poem = self.poet.run()
# # # #         poetry_type = self.triage.run(poem)

# # # #         if poetry_type == "lyric":
# # # #             return self.lyric.run(poem)
# # # #         elif poetry_type == "narrative":
# # # #             return self.narrative.run(poem)
# # # #         elif poetry_type == "dramatic":
# # # #             return self.dramatic.run(poem)
# # # #         else:
# # # #             return "❌ Could not determine poetry type."

# # # # # ------------------ Run the App ------------------
# # # # if __name__ == "__main__":
# # # #     agent = ParentAgent()
# # # #     output = agent.run()
# # # #     print(output)

# # # # import os
# # # # import random
# # # # from dotenv import load_dotenv

# # # # # OpenRouter Setup
# # # # from openai import AsyncOpenAI
# # # # from agents import OpenAIChatCompletionsModel, RunConfig

# # # # # 📌 Load API Key from .env
# # # # load_dotenv()
# # # # openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# # # # if not openrouter_api_key:
# # # #     raise ValueError("❌ OPENROUTER_API_KEY missing in .env")

# # # # # External Client Setup
# # # # external_client = AsyncOpenAI(
# # # #     api_key=openrouter_api_key,
# # # #     base_url="https://openrouter.ai/api/v1"
# # # # )

# # # # model = OpenAIChatCompletionsModel(
# # # #     model="deepseek/deepseek-v3-base:free",
# # # #     openai_client=external_client
# # # # )

# # # # config = RunConfig(
# # # #     model=model,
# # # #     model_provider=external_client,
# # # #     tracing_disabled=True
# # # # )

# # # # # ------------------ Poet Agent ------------------
# # # # class PoetAgent:
# # # #     def run(self):
# # # #         poems = [
# # # #             """You left without a final word,  
# # # # Now silence is all that’s heard.  
# # # # Each tear I cry, a memory dies,  
# # # # Love faded under endless skies.""",

# # # #             """I held your name inside my heart,  
# # # # But time has torn that love apart.  
# # # # The dreams we dreamt have turned to dust,  
# # # # Now I wander through this world unjust.""",

# # # #             """In every smile I try to fake,  
# # # # There hides a heart you chose to break.  
# # # # Your voice still echoes in the rain,  
# # # # A melody wrapped deep in pain.""",

# # # #             """I waited where we used to meet,  
# # # # But all I felt was empty street.  
# # # # Your shadow danced and disappeared,  
# # # # Just like the love I once held dear."""
# # # #         ]

# # # #         poem = random.choice(poems)
# # # #         print("📝 Randomly generated sad love poem:\n")
# # # #         print(poem)
# # # #         return poem

# # # # # ------------------ Triage Agent ------------------
# # # # class TriageAgent:
# # # #     def run(self, poem):
# # # #         lower_poem = poem.lower()
# # # #         if any(word in lower_poem for word in ['feeling', 'love', 'heart', 'sad', 'joy', 'alone']):
# # # #             return "lyric"
# # # #         elif any(word in lower_poem for word in ['once', 'there was', 'king', 'story', 'river', 'hero']):
# # # #             return "narrative"
# # # #         elif any(word in lower_poem for word in ['stage', 'dialogue', 'act', 'audience', 'character']):
# # # #             return "dramatic"
# # # #         else:
# # # #             return "lyric"  # fallback

# # # # # ------------------ Lyric Analyst ------------------
# # # # class LyricAnalyst:
# # # #     def run(self, poem):
# # # #         return f"""🔍 Analyzing your poem...

# # # # Lyric Poetry - This poem isn’t just words — it’s the echo of a heart breaking silently.
# # # # As the light fades, so does the last bit of hope the poet was holding on to.
# # # # It speaks of a love that once brought warmth, now leaving behind only cold memories.
# # # # The “sun” and its fading light aren’t just nature — they’re a reflection of the poet’s soul dimming.
# # # # And when night falls, it’s not just darkness outside — it’s the storm of grief within.
# # # # Each line carries the ache of something precious that slipped away.
# # # # This is not just lyric poetry... this is someone bleeding gently through their pen.

# # # # 🧠 Last agent used: Lyric Poetry Analyst

# # # # 📜 Your Poem:
# # # # {poem}
# # # # """

# # # # # ------------------ Narrative Analyst ------------------
# # # # class NarrativeAnalyst:
# # # #     def run(self, poem):
# # # #         return f"""📖 Analyzing your poem...

# # # # Narrative Poetry - This poem tells a story.
# # # # It involves characters and a clear sequence of events.
# # # # The poet narrates a journey, a conflict, or a moment in time.
# # # # Words like "once", "journey", or "battle" indicate storytelling form.
# # # # There is a clear beginning, middle, and possible ending.

# # # # 🧠 Last agent used: Narrative Poetry Analyst

# # # # 📜 Your Poem:
# # # # {poem}
# # # # """

# # # # # ------------------ Dramatic Analyst ------------------
# # # # class DramaticAnalyst:
# # # #     def run(self, poem):
# # # #         return f"""🎭 Analyzing your poem...

# # # # Dramatic Poetry - This poem is written as if for performance.
# # # # The speaker seems to be talking to an audience.
# # # # Lines may be in dialogue form or monologue.
# # # # It explores inner thoughts through spoken drama.

# # # # 🧠 Last agent used: Dramatic Poetry Analyst

# # # # 📜 Your Poem:
# # # # {poem}
# # # # """

# # # # # ------------------ Parent Agent (Triage + Route) ------------------
# # # # class ParentAgent:
# # # #     def __init__(self):
# # # #         self.poet = PoetAgent()
# # # #         self.triage = TriageAgent()
# # # #         self.lyric = LyricAnalyst()
# # # #         self.narrative = NarrativeAnalyst()
# # # #         self.dramatic = DramaticAnalyst()

# # # #     def run(self):
# # # #         poem = self.poet.run()
# # # #         poetry_type = self.triage.run(poem)

# # # #         if poetry_type == "lyric":
# # # #             return self.lyric.run(poem)
# # # #         elif poetry_type == "narrative":
# # # #             return self.narrative.run(poem)
# # # #         elif poetry_type == "dramatic":
# # # #             return self.dramatic.run(poem)
# # # #         else:
# # # #             return "❌ Could not determine poetry type."

# # # # # ------------------ Run the App ------------------
# # # # if __name__ == "__main__":
# # # #     agent = ParentAgent()
# # # #     output = agent.run()
# # # #     print(output)

# # # # from dotenv import load_dotenv
# # # # import os
# # # # from agents import Agent,Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig


# # # # load_dotenv()

# # # # openrouter_api_key = os.getenv('OPENROUTER_API_KEY')

# # # # if not openrouter_api_key:
# # # #     raise ValueError(" OPENROUTER is not set. Please ensure it is defined in your .env file.")

# # # # external_client = AsyncOpenAI(
# # # #     api_key= openrouter_api_key,
# # # #     base_url="https://openrouter.ai/api/v1",
# # # # )

# # # # model = OpenAIChatCompletionsModel(
# # # #     model="deepseek/deepseek-v3-base:free",
# # # #     openai_client=external_client
# # # # )

# # # # config = RunConfig(
# # # #     model=model,
# # # #     model_provider=external_client,
# # # #     tracing_disabled=True
# # # # )


# # # # import streamlit as st
# # # # import requests
# # # # import os
# # # # from dotenv import load_dotenv

# # # # # =============== AGENT SDK SETUP ===============
# # # # from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# # # # load_dotenv()

# # # # openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
# # # # if not openrouter_api_key:
# # # #     raise ValueError("OPENROUTER_API_KEY is missing in your .env file.")

# # # # # OpenRouter client setup
# # # # external_client = AsyncOpenAI(
# # # #     api_key=openrouter_api_key,
# # # #     base_url="https://openrouter.ai/api/v1",
# # # # )

# # # # model = OpenAIChatCompletionsModel(
# # # #     model="deepseek/deepseek-v3-base:free",
# # # #     openai_client=external_client
# # # # )

# # # # config = RunConfig(
# # # #     model=model,
# # # #     model_provider=external_client,
# # # #     tracing_disabled=True
# # # # )

# # # # # =============== ULTRAMSG SETUP ===============
# # # # INSTANCE_ID = "instance133113"
# # # # TOKEN = "3h7ew67tofc6cic2"
# # # # API_URL = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"

# # # # # =============== STREAMLIT UI ===============
# # # # st.set_page_config(page_title="OpenRouter Agent WhatsApp Sender", page_icon="📤")
# # # # st.title("🤖 AI Agent to WhatsApp Sender")
# # # # st.markdown("Write a message prompt, generate response via Agent, and send to WhatsApp using UltraMsg.")

# # # # number = st.text_input("📱 WhatsApp Number (without +, e.g. 92345XXXXXXX)")
# # # # prompt = st.text_area("🧠 What should the agent generate?", height=150)

# # # # if st.button("🎨 Generate with Agent"):
# # # #     if prompt:
# # # #         with st.spinner("Asking Agent..."):
# # # #             # Run agent
# # # #             runner = Runner(config=config)
# # # #             response = runner.run(prompt)
# # # #             ai_message = response.output
# # # #             st.success("✅ Agent Response:")
# # # #             st.write(ai_message)
# # # #             st.session_state.generated = ai_message
# # # #     else:
# # # #         st.warning("Please write a prompt!")

# # # # if "generated" in st.session_state:
# # # #     if st.button("🚀 Send to WhatsApp"):
# # # #         full_number = f"+{number}"
# # # #         payload = {
# # # #             "token": TOKEN,
# # # #             "to": full_number,
# # # #             "body": st.session_state.generated
# # # #         }

# # # #         res = requests.post(API_URL, data=payload)
# # # #         result = res.json()

# # # #         if result.get("sent"):
# # # #             st.success("✅ Message sent successfully!")
# # # #         else:
# # # #             st.error(f"❌ Failed to send message: {result}")


# # # import streamlit as st
# # # from dotenv import load_dotenv
# # # import os
# # # import requests

# # # from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# # # # Load .env
# # # load_dotenv()

# # # # Set OpenRouter API key
# # # openrouter_api_key = os.getenv('OPENROUTER_API_KEY')
# # # if not openrouter_api_key:
# # #     raise ValueError("OPENROUTER_API_KEY not set in .env file.")

# # # # Set up OpenAI model through OpenRouter
# # # external_client = AsyncOpenAI(
# # #     api_key=openrouter_api_key,
# # #     base_url="https://openrouter.ai/api/v1",
# # # )

# # # model = OpenAIChatCompletionsModel(
# # #     model="deepseek/deepseek-v3-base:free",
# # #     openai_client=external_client
# # # )

# # # # Run configuration
# # # config = RunConfig(
# # #     model=model,
# # #     model_provider=external_client,
# # #     tracing_disabled=True
# # # )

# # # # Create agent
# # # agent = Agent()

# # # # WhatsApp API credentials (public key here)
# # # ultramsg_token = "3h7ew67tofc6cic2"
# # # instance_id = "instance133113"
# # # ultramsg_url = f"https://api.ultramsg.com/{instance_id}/messages/chat"

# # # # Streamlit UI
# # # st.set_page_config(page_title="AI WhatsApp Sender", page_icon="🤖")
# # # st.title("💬 AI WhatsApp Assistant using UltraMsg + OpenRouter")

# # # phone = st.text_input("📞 Phone Number (with country code)", placeholder="+923001234567")
# # # user_msg = st.text_area("📝 Your Message", height=150)

# # # if st.button("🚀 Send AI Reply on WhatsApp"):
# # #     if not phone or not user_msg:
# # #         st.warning("Phone number aur message dono bharna zaroori hai.")
# # #     else:
# # #         # Run AI agent
# # #         with st.spinner("🤖 AI soch raha hai..."):
# # #             response = agent.run(user_msg, config=config)

# # #         st.success("✅ AI Response Ready!")
# # #         st.write("**AI Reply:**", response)

# # #         # WhatsApp API call
# # #         payload = {
# # #             "token": ultramsg_token,
# # #             "to": phone,
# # #             "body": response
# # #         }

# # #         res = requests.post(ultramsg_url, data=payload)

# # #         if res.status_code == 200:
# # #             st.success("📤 Message WhatsApp pe bhej diya gaya!")
# # #         else:
# # #             st.error(f"❌ Error sending message: {res.text}")


# # import streamlit as st
# # import requests
# # from agents import AgentRunner, Agent

# # # --- WhatsApp API Config ---
# # WHATSAPP_TOKEN = "3h7ew67tofc6cic2"  # public rakhna chah rahe ho
# # WHATSAPP_INSTANCE = "instance133113"
# # WHATSAPP_URL = f"https://api.ultramsg.com/{WHATSAPP_INSTANCE}/messages/chat"

# # # Dummy Users
# # users = [
# #     {"name": "Aisha", "age": 20, "gender": "female"},
# #     {"name": "Ali", "age": 22, "gender": "male"},
# #     {"name": "Sara", "age": 18, "gender": "female"},
# #     {"name": "Ahmed", "age": 25, "gender": "male"},
# # ]

# # # --- Agent Task Definition ---
# # class MatchAgent(Agent):
# #     def __init__(self):
# #         super().__init__(name="Matchmaking Agent", description="Suggests best partner.")

# #     def run(self, name, age, gender):
# #         age = int(age)
# #         for user in users:
# #             if user["gender"] != gender and user["age"] <= age:
# #                 return {
# #                     "message": f"Hey {name}! Tumhare liye best match mila: {user['name']} ({user['gender']}, {user['age']} years old). 💖"
# #                 }
# #         return {"message": f"Sorry {name}, abhi koi perfect match available nahi hai 😔"}

# # # --- WhatsApp Message Sender ---
# # def send_whatsapp_message(name, to, message):
# #     payload = f"token={WHATSAPP_TOKEN}&to={to}&body=Hi {name}, {message}"
# #     headers = {'content-type': 'application/x-www-form-urlencoded'}
# #     response = requests.post(WHATSAPP_URL, data=payload, headers=headers)
# #     return response.text

# # # --- Streamlit UI ---
# # st.set_page_config(page_title="💘 Dil ka Rishta", page_icon="💌")
# # st.title("💘 Dil ka Rishta - Rishtay Agent with WhatsApp")

# # with st.form("match_form"):
# #     name = st.text_input("👤 Your Name")
# #     age = st.number_input("🎂 Your Age", min_value=18, max_value=99)
# #     gender = st.selectbox("🚻 Your Gender", ["male", "female"])
# #     to = st.text_input("📱 Your WhatsApp Number (e.g., +923001234567)")
# #     submit = st.form_submit_button("🔍 Find Match & Send WhatsApp")

# # if submit:
# #     with st.spinner("🤖 Rishta dhoondha ja raha hai..."):
# #         agent = MatchAgent()
# #         runner = AgentRunner(agent)
# #         result = runner.run(name=name, age=age, gender=gender)
# #         match_message = result["message"]

# #         # WhatsApp Message bhejo
# #         response = send_whatsapp_message(name, to, match_message)

# #     st.success("✅ Rishta message WhatsApp pe bhej diya gaya!")
# #     st.info(f"📬 Response: {response}")

# import streamlit as st
# import asyncio
# from connection import generate_message

# # Streamlit UI
# st.set_page_config(page_title="Rishta WhatsApp Message", layout="centered")
# st.title("📩 Islamic Rishta WhatsApp Message Sender")

# st.markdown("**Prompt likho:** (e.g. WhatsApp per aik Islamic rishta wali message likho)")
# prompt = st.text_area("📝 Prompt", value="WhatsApp per aik Islamic rishta wali message likho.")

# if st.button("🔮 Generate Message"):
#     if prompt.strip() == "":
#         st.warning("⛔ Please enter a prompt.")
#     else:
#         with st.spinner("Gemini soch raha hai..."):
#             try:
#                 # Run the async Gemini call safely
#                 loop = asyncio.new_event_loop()
#                 asyncio.set_event_loop(loop)
#                 message = loop.run_until_complete(generate_message(prompt))
#                 loop.close()

#                 st.success("✅ Message tayar hai!")
#                 st.text_area("📤 Message", value=message, height=200)
#             except Exception as e:
#                 st.error(f"⚠️ Error: {e}")



# import streamlit as st
# import requests
# import os
# from dotenv import load_dotenv

# # Load API key from .env
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# st.title("📲 Gemini WhatsApp Message Sender")

# # UltraMsg Inputs
# instance_id = st.text_input("🔧 UltraMsg Instance ID", value="instance133113")
# token = st.text_input("🔐 UltraMsg Token", value="3h7ew67tofc6cic2", type="password")
# receiver = st.text_input("📱 WhatsApp Number", placeholder="+923001234567")

# # Gemini Prompt
# prompt = st.text_area("🧠 Describe your message (Gemini Prompt)", "Islamic rishta wali WhatsApp message likho")

# # Generate message from Gemini API
# def generate_message_from_gemini(prompt):
#     url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
#     headers = {"Content-Type": "application/json"}
#     data = {
#         "contents": [{"parts": [{"text": prompt}]}]
#     }
#     response = requests.post(url, headers=headers, json=data)
#     if response.status_code == 200:
#         return response.json()['candidates'][0]['content']['parts'][0]['text']
#     else:
#         st.error(f"❌ Gemini API Error: {response.text}")
#         return ""

# # Button to generate
# if st.button("✨ Generate Message with Gemini"):
#     if not prompt:
#         st.warning("⚠️ Please enter a prompt.")
#     else:
#         gen_msg = generate_message_from_gemini(prompt)
#         st.session_state.generated_msg = gen_msg
#         st.success("✅ Message generated!")
#         st.text_area("📨 Generated Message", value=gen_msg, height=150, key="generated_msg")

# # Final message input
# final_msg = st.text_area("✍️ Final Message to Send", value=st.session_state.get("generated_msg", ""), height=150)

# # Send via WhatsApp
# if st.button("📤 Send WhatsApp Message"):
#     if not (instance_id and token and receiver and final_msg):
#         st.warning("⚠️ Fill all fields.")
#     else:
#         url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
#         payload = f"token={token}&to={receiver}&body={final_msg}"
#         headers = {'content-type': 'application/x-www-form-urlencoded'}
#         payload = payload.encode('utf8').decode('iso-8859-1')
#         response = requests.post(url, data=payload, headers=headers)
#         if response.status_code == 200:
#             st.success("✅ Message sent on WhatsApp!")
#         else:
#             st.error(f"❌ Failed to send: {response.text}")


import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Page config
st.set_page_config(page_title="Gemini WhatsApp Sender", page_icon="💬", layout="centered")

# Custom CSS for better UI
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .stTextInput > div > div,
        .stTextArea > div > textarea {
            border: 1px solid #ced4da;
            border-radius: 0.5rem;
        }
        .stButton > button {
            border-radius: 0.5rem;
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("<h1 style='text-align: center; color: #333;'>💬 Gemini WhatsApp Message Sender</h1>", unsafe_allow_html=True)
st.markdown("### 👇 Fill the details below to generate and send a WhatsApp message")

# Input fields section
with st.container():
    st.subheader("🔧 WhatsApp API Settings")
    instance_id = st.text_input("Instance ID", value="instance133113")
    token = st.text_input("API Token", value="3h7ew67tofc6cic2", type="password")
    receiver = st.text_input("Recipient Number", placeholder="+923001234567")

st.markdown("---")

# Prompt area
with st.container():
    st.subheader("🧠 Gemini Prompt")
    prompt = st.text_area("Describe what kind of message you want Gemini to generate", 
                          "e.g. Islamic rishta wali WhatsApp message likho")

# Gemini message generator
def generate_message_from_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        st.error(f"❌ Gemini API Error: {response.text}")
        return ""

# Generate button
if st.button("✨ Generate Message with Gemini"):
    if not prompt:
        st.warning("⚠️ Please enter a prompt.")
    else:
        gen_msg = generate_message_from_gemini(prompt)
        st.session_state.generated_msg = gen_msg
        st.success("✅ Message generated!")
        st.text_area("📨 Generated Message", value=gen_msg, height=150, key="generated_msg")

# Final message (editable)
st.markdown("---")
st.subheader("✍️ Final Message to Send")
final_msg = st.text_area("Review or edit your message before sending", value=st.session_state.get("generated_msg", ""), height=150)

# Send button
if st.button("📤 Send WhatsApp Message"):
    if not (instance_id and token and receiver and final_msg):
        st.warning("⚠️ Please fill in all fields.")
    else:
        url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
        payload = f"token={token}&to={receiver}&body={final_msg}"
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        payload = payload.encode('utf8').decode('iso-8859-1')
        response = requests.post(url, data=payload, headers=headers)
        if response.status_code == 200:
            st.success("✅ WhatsApp message sent successfully!")
        else:
            st.error(f"❌ Failed to send message: {response.text}")
