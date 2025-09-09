# LLM Azure Deployment
import asyncio
from langchain_openai import AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_postgres import PGVector

from dotenv import load_dotenv
import os

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
    

if __name__ == "__main__":
    asyncio.run(main())
