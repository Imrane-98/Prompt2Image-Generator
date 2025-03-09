# Prompt2Image-Generator

Prompt2Image-Generator converts text prompts into images using Hugging Face's **sd-community/sdxl-flash** model and a Gradio interface. API keys are securely managed via environment variables.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Prompt2Image-Generator.git
   cd Prompt2Image-Generator
2. **Install dependencies:** <br>
pip install gradio requests huggingface_hub Pillow transformers

3. **Set your Hugging Face API key:** <br>
export HF_API_KEY="your_api_key_here"

4. **Run the application:** <br>
   python app.py
