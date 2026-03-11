# Mini-RAG-App

This is a mimnaml implementation of the RAG model for question answering.

## Requirments 
python 3.8 or later 

## Install Py using MiniConda 

1) Download and install MiniConda from [here] (https://www.anaconda.com/docs/getting-started/miniconda/main#quick-command-line-install)
2) Create a new environment using the following command:
``` bash
$ conda create -n mini-rag python=3.10
```
3) acivate the envitoment 
``` bash
$ conda activate mini-rag
```

## Installation
### Install the required packages

``` bash
$ pip install -r requirements.txt
```
### Setup the environment variables

``` bash
$ cp .env.example .env
```

Set your environment variables in the .env file. Like OPENAI_API_KEY value.

# Run the FastAPI server (Development Mode)
``` bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```