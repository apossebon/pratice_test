# LLM Azure Deployment
import asyncio
from xml.parsers.expat import model
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings, ChatOpenAI


from dotenv import load_dotenv
import os

from pydantic import SecretStr

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env

async def main():
    print("Hello from pratice-test!")

    chat = AzureChatOpenAI(
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"), 
        azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        model=os.getenv("AZURE_OPENAI_MODEL_NAME"),
        temperature=0,
        max_retries=3, 
        streaming=True
    )

    embeddings = AzureOpenAIEmbeddings(
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        model=os.getenv("AZURE_DEPLOYMENT_NAME_VECTORSTORE"),
        chunk_size=1000,
        max_retries=3,
        validate_base_url=False
    )


    llm_docker = ChatOpenAI(
        base_url=os.getenv("base_url_Docker"),
        api_key="localdev",
        model=os.getenv("DOCKER_LLM_MODEL"),
        max_tokens=4098,
        temperature=0.7,
        max_retries=3,
        streaming=True
    )

    for chunk in llm_docker.stream("Se eu trabalho 40 horas semanais e ganho por hora 40 dolares, qual o meu salário mensal? sendo que o valor do dolar é de 5.4 reais"):
        print(chunk.content, end='', flush=True)
    

if __name__ == "__main__":
    asyncio.run(main())
