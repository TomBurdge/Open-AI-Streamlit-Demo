### Streamlit with OpenAI

OpenAI does some amazing things in the ChatGPT front-end app, but what is the easiest way to make a front-end app that uses ChatGPT?

Enter Streamlit. Streamlit is an extremely streamlined tool for simple web apps with python.

This repo is an example app which receives a user input.

### The use case
Let's say you work at a large company and you want to know the parent brand of a company.

This can be useful for comparing my company's share to its competitors - if I work for Proctor & Gamble I don't *only* want to know my market share against Ben&Jerry's; I want to know my market share against Unilever. If we have an app which can tell us the parent brand, we can find the parent company even if our data supplier hasn't given it to us.

I have a brand, MountainDew, but what is the parent brand?

In this case, you may know the parent brand is PepsiCo.

But let's try a harder example, who is the parent brand of Chattem, Inc.

Probably only domain-specific specialists know that Chattem was acquired by Sanofi in 2009.

But OpenAI, which was effectively trained on the entire internet, does know this.

## Prompt safety handling

A common issue with any app is that users, or those impersonating authorised users, try to misuse the app.

The most famous example of this is SQL insertion - where attackers try to insert unwanted behaviour such as """DELETE TABLE USERS""" into a SQL statement.

This can happen with LLM prompts too - a user could try to get OpenAI to expose a password or behave discriminatorily.

Probably the easiest way to handle this is to use an LLM to screen the message before it is actually processed.

In streamlit_app.py, I have implemented a very simple message to protect against malicious or deceptive prompts being sent to the main model.

## How to use this App

Do you want to use this app?

Go to **placeholder.com** to use this app hosted on streamlit community cloud.
