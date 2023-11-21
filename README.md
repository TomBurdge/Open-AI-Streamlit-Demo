# Streamlit with OpenAI

OpenAI has revolutionized the way we interact with AI through the ChatGPT front-end application. But how can one create a user-friendly front-end application that leverages ChatGPT's capabilities? The answer lies in Streamlit.

Streamlit is an incredibly efficient framework for building simple web applications using Python. This repository provides an example of such an application, designed to receive and process user input.

## The Use Case

Imagine you're employed at a large corporation and need to find the parent company of a specific brand. This information is crucial for market share analysis, especially when comparing your company's performance against its competitors. For instance, if you're working at Proctor & Gamble, it's not just about understanding your market share in comparison to Ben & Jerry's; you need to see the bigger picture against Unilever.

Consider a brand like MountainDew. You might know its parent company is PepsiCo. But what about a less-known example, such as Chattem, Inc.? Not everyone knows that Chattem was acquired by Sanofi in 2009. This is where OpenAI's extensive training on a vast array of internet sources becomes invaluable.

## Prompt Safety Handling

One of the challenges with any application is ensuring that it is not misused, either by regular users or those impersonating authorized users. A classic example of such misuse is SQL injection, where attackers input destructive commands like `"""DELETE TABLE USERS"""` into SQL statements.

Similar risks exist with Large Language Models (LLMs) where prompts might be crafted to extract sensitive information or promote discriminatory behavior. A practical solution is to use an LLM to screen the messages before they are processed by the main model.

In the `streamlit_app.py` file, you'll find a simple method to safeguard against malicious or deceptive prompts.

If I was particularly concerned with making a production-ready and safe app, I would also use some API calls. But this is just a fun demo.

## How to Use This App

Interested in using this application?

Visit [This link](https://parent-brands-open-ai-app-demo-cjwqtbpluasoalp3n4vz9q.streamlit.app/) to access the app, hosted on the Streamlit Community Cloud. At present, to access you will need a password.

I don't want to flood streamlit's servers (this is hosted on StreamLit Community Cloud) or my own API key with traffic.

If you want to access the site, then enter when prompted:
- The two word magical phrase that opens the mouth of a cave in Ali Baba and the Fourty Thieves. Lower case and connected with hpyhens.
- Connect the first phrase, with a hyphen, to the year (AD) that the siege of Amiens occured.

If you cannot use this app, please raise an issue. It is likely that a spending limit has been reached, or you haven't used the right the password.
