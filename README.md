# BRBuddy Backend Proxy

__NOTE__: This repository documents a hackathon component written in a microsoft hackathon that took part between the 17th-19th of july 2024 in Munich. The used azure components referenced in this repository might not be active anymore.

The BRBuddy chat is a RAG system for employees of the Bayerischer Rundfunk the provide media house internal information. To serve the BRBuddy frontend this backend proxy project was written.

## Local setup

Create a virtualenv (pyenv is just a suggestion. Use the tool you like.)

`pyenv virtualenv 3.10 brbuddy-api-service`

Activate the virtual environment:

`pyenv activate brbuddy-api-service`

install dependencies using

`pip install -r requirements.txt`

## Usage

Run the application by running `python api.py`

## Local Setup

This is a python project. Use 

## Deployement

The deployment configuration is related the cloud infrastructure of the Bayerischer Rundfunk. Adjust it at necessary to your infrastructure.

## API Endpoints

The project's APIs are document via the endpoint [/v1/docs](http://localhost:3000/docs)
