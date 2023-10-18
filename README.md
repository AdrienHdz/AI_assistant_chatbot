# Lexi, AI-Powered Customer Support

[![CI](https://github.com/AdrienHdz/AI_assistant_chatbot/actions/workflows/CI.yml/badge.svg)](https://github.com/AdrienHdz/AI_assistant_chatbot/actions/workflows/CI.yml)

<p align="center">
  <img src="https://github.com/AdrienHdz/AI_assistant_chatbot/blob/main/avatar.gif?raw=true" alt="Alt Text">
</p>

## Prerequites

Ensure you have the following environment variables:
- APP_OPENAI_API_KEY, create an account on [OpenAI](https://www.openai.com) to get your API key
- APP_REPLICATE_API_TOKEN, create an account on [Replicate](https://replicate.com/) to get your API key
- APP_ELEVENLABS_API_KEY, create an account on [Elevenlabs](https://elevenlabs.io/) to get your API key
- APP_GCP_PROJECT_ID, it is the ID of your project in Google Cloud Platform(https://cloud.google.com/?hl=en)
- APP_VERTEXAI_LOCATION, use a geographic location that is compatible with Vertex AI (I'm using us-central1)

Make sure to login in GCP with the command:
```sh
gcloud auth application-default login
```
This will allow the backend running inside the Docker container to use these credentials to authenticate with Google Cloud Services.

## Use docker-compose to run the project 

Ensure that you have both Docker and docker-compose installed on your system:
I'm using a Builtkit in the backend Dockerfile. You must therefore active the correspond environment variables to build the docker images.
 ```sh
export DOCKER_BUILDKIT=1
export COMPOSE_DOCKER_CLI_BUILD=1
```  

To start the application, simply run:
 ```sh
make dc-up
```  
## Stack

- [FastApi](https://fastapi.tiangolo.com/) - A modern, fast, web framework for building APIs with Python 3.8+
- [Angular](https://angular.io/) - An application-design framework and development platform for creating efficient and sophisticated singled-page apps.
- [TailwindCSS](https://tailwindcss.com/) - a utility-first CSS framework for rapidly building modern websites.
- [Docker](https://www.docker.com/) - a software to build and run container applications.
- [Redis](https://redis.io/) - An open source, in-memory data structure store, used as a database, cache and message broker.

## Project structure
```
$PROJECT_ROOT
│   # Python backend using FastApi and Redis
├── backend
│   # Angular and tailwind CSS frontend 
├── frontend
│   # Docker compose config files 
├── docker-compose
│   # An example to fine tune gpt3.5 turbo with a sample of data
└── example-fine-tuning
```

## License

MIT License.

You can reuse any part of my work and code for free without notifying me by forking this project under the following conditions:

- Attribution: You must give appropriate credit, provide a link to my repository (https://github.com/AdrienHdz/AI_assistant_chatbot) or to my website (https://www.adrienhernandez.com/).
- For example: "This project is built based on Adrien Hernandez's AI assistant chatbot project."

