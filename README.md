<h1 align="center">
📖 GPT-Engineer-Streamlit-App
</h1>

![UI](ui.PNG?raw=true)

## [GPT-Engineer](https://github.com/AntonOsika/gpt-engineer)

This app is created by GPT_engineer with below prompt. Follow the Guidelines in above repo.

`We are writing a streamlit app with csv upload function and basis data analysis dashboard`

The Poetry Environment is created by Humane.

## 🔧 Features

- App Created by [`GPT-Engineer`](https://github.com/AntonOsika/gpt-engineer)
- Deployed on Streamlit

This repo contains an `main.py` file which has a template for a chatbot implementation.

## Adding your chain
To add your chain, you need to change the `load_chain` function in `main.py`.
Depending on the type of your chain, you may also need to change the inputs/outputs that occur later on.


## 💻 Running Locally

1. Clone the repository📂

```bash
git clone https://github.com/amjadraza/langchain-streamlit-docker-template.git
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment🔨

```bash
poetry install
poetry shell
```

3. Run the Streamlit server🚀

```bash
streamlit run demo_app/main.py 
```

Run App using Docker
--------------------
This project includes `Dockerfile` to run the app in Docker container. In order to optimise the Docker Image
size and building time with cache techniques, I have follow tricks in below Article 
https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0

Build the docker container

``docker  build . -t gpt-engineer-streamlit-app:latest ``

To generate Image with `DOCKER_BUILDKIT`, follow below command

```DOCKER_BUILDKIT=1 docker build --target=runtime . -t gpt-engineer-streamlit-app:latest```

1. Run the docker container directly 

``docker run -d --name gpt-engineer-streamlit-app:latest -p 8080:8080 langchain-chat-app ``

2. Run the docker container using docker-compose (Recommended)

``docker-compose up``


Deploy App on Streamlit Public Cloud
------------------------------------
This app can be deployed on Streamlit Public Cloud using GitHub. Below is the Link to 
Publicly deployed App

https://gpt-egineer-dashboard.streamlit.app/


## DISCLAIMER

This is a template App, when using with openai_api key, you will be charged a nominal fee depending
on number of prompts etc.