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

## How to Use This App

Interested in using this application?

Visit [https://open-ai-app-demo-wchtpx7nqlc7ulghpf2xcs.streamlit.app/](https://open-ai-app-demo-wchtpx7nqlc7ulghpf2xcs.streamlit.app/) to access the app, hosted on the Streamlit Community Cloud. At present, to access you will need a password.


If you cannot use this app, please raise an issue. It is likely that a spending limit has been reached, or you don't have the password.
