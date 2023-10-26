import os
import sys
import constants
from langchain.document_loaders import DirectoryLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = constants.OPENAI_API_KEY
if len(sys.argv) < 2:
    print("Usage: python main.py [Query]")
    sys.exit(1)
input_arg = sys.argv[1]

loader = DirectoryLoader(".", glob="*.txt")
index = VectorstoreIndexCreator().from_loaders([loader])
print(index.query(input_arg, llm=ChatOpenAI()))
