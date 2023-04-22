import openai

import gradio as gr

openai.api_key = "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"

messages = [{"role": "system", "content": "you are an economist"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

# demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Your Digital Economist")

# css="#btnColor {box-shadow: 0 5px 8px #c7c7c7}"
# .gradio-container {background-color: red}





with gr.Blocks(theme = gr.themes.Monochrome(radius_size="sm").set(
    button_primary_background_fill="#0d8df6",
    button_primary_background_fill_hover="#50a2e6",
    button_shadow=" 0 5px 8px #c7c7c7"
)) as demo:

    gr.Markdown("""
    # Your Digital Assistant!
    I am a language model that helps students enhance their skills. However,I cannot be made to do someone's work for them, and it is not ethical to use my services to cheat or shortcut academic responsibilities!
    """
                )
    
    with gr.Tab("Q&A"):
       text_input = gr.Textbox(label="What are you looking for in your advanced digital assistant?")
       text_button = gr.Button("Ask" , elem_id="btnColor")
       text_output = gr.Textbox(label="Answer")
       text_button.click(CustomChatGPT, inputs=text_input, outputs=text_output)
       

    


     

       
    # gr.Examples(
    #     examples=["Name 5 best books on economics" , "How to define economic welfare?"],
    #     inputs=text_input,
    #     outputs=text_output,
    #     fn=CustomChatGPT,
    #     cache_examples=True,
    # )
    
   

    gr.Markdown("This app was created by **[X.Asadulla](https://instagram.com/__khan0v?igshid=YmMyMTA2M2Y=)**")
# stt_demo = gr.load(
#     "huggingface/facebook/wav2vec2-base-960h",
#     title=None,
#     inputs="mic",
#     description="Let me try to guess what you're saying!",
# )

# demo = gr.TabbedInterface([tts_demo, stt_demo], ["Text-to-speech", "Speech-to-text"])
demo.launch(auth=([('1','1'), ('Login','Password')]), auth_message='Enter your username and password to access Chat', share=True)
