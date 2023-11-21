import streamlit as st
from openai import OpenAI

st.title("Product Harmonisation with OpenAI")


openai_key = st.secrets["OPENAI_API_KEY"]

client = OpenAI(
    api_key=openai_key,
)

system_message = """
You are a helpful assistant for finding out the parent of an FMCG brand/manufacturer.
You always respond with the parent brand/manufacturer of a brand/manufacturer that you receive. You also return a confidence score between 0 and 1.
For example, the parent brand of Johnson's Baby is Kenvue.
You may receive further information, such as the geographic location of this brand, but not always.
"""

text = st.text_area("Enter a System Message to instruct OpenAI")
analyze_button = st.button("Analyze Text")

if analyze_button:
    message = [
        {
            "role": "system",
            "content": f"{system_message}",
        },
        {
            "role": "user",
            "content": f"Please find the parent of the following: {text}",
        },
    ]
    response = client.chat.completions.create(
        messages=message,
        model="gpt-3.5-turbo",
    )
    result = response.choices[0].message.content.strip()
    st.write(result)
