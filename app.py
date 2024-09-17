import gradio as gr
import google.generativeai as genai
import os

import argparse

def use_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text

def config_chatbot(message, history):
    response = model.generate_content(message)
    return response.text

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="select application")

    parser.add_argument("--model", type=str, help="choose model for your application", default="gemini-1.5-flash")
    parser.add_argument("--application_type", type=str, help="choose application", default="chatbot")
    parser.add_argument("--ui", default="gradio")
    args = parser.parse_args()
    
    genai.configure(api_key=os.environ["API_KEY"])
    model = genai.GenerativeModel(args.model)
    
    if args.application_type == "text-generation":
        demo1 = gr.Interface(
            fn=use_gemini,
            inputs=["text"],
            outputs=["text"],
        )
        demo1.launch()
    elif args.application_type == "chatbot":  
        gr.ChatInterface(config_chatbot).launch()
