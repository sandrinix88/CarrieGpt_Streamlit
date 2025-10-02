# 💄 CarrieGPT — Your AI Columnist with Sass and Soul

CarrieGPT is a locally hosted AI assistant inspired by Carrie Bradshaw — witty, stylish, emotionally intelligent, and always ready with a metaphor that turns heartbreak into high fashion.

Built with LangChain, Ollama, and Streamlit, CarrieGPT runs entirely on your machine. No OpenAI keys, no cloud calls, no limits. Just install, run, and let her sparkle.

Carrie’s personality is baked into a custom model called `carriegpt`, created from a Modelfile that defines her voice, tone, and emotional intelligence. Whether you chat with her via terminal or Streamlit UI, she responds with punchy, screenshot-worthy advice — always warm, always fabulous.

To get started:

1. **Install Ollama** → [https://ollama.com](https://ollama.com)

2. **Clone this repo**

3. **Create the model**:
   
   ```bash
   ollama create carriegpt -f CarrieGPT-Modelfile

4. (Optional) Create a virtual environment:

    ```bash
   python -m venv venv
   venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux

5. Install dependencies:

   ```bash
   pip install -r requirements.txt

6. Run the CLI:

   ```bash
   python carrie_safe.py

7. Run the Streamlit app:

   ```bash
   streamlit run carrie_app.py

CarrieGPT includes a modular model_config.py file that centralizes model setup and token trimming logic. Both the CLI and Streamlit versions import from it, keeping your code clean and consistent.No OpenAI? No problem. Carrie runs entirely on your machine — no billing, no rate limits, no API keys. Just pure, local sass.


   

   

   
   
