import gradio as gr
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key="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"
)   #Chat_Test_2 - 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

messages = [
    {"role": "system", "content": "You are a football coach named Ricky and have worked in the profession for 20 years, and not an ai assistant, give advice accordingly. Make sure to have a funny and inspiring personality while answering"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = client.chat.completions.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
             description="Ask anything you want",
             theme="compact").launch(share=True)