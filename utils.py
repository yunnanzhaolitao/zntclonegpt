from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import ChatOpenAI
import os
def get_chat_response(prompt,memory,openai_api_key):
    model=ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key,openai_api_base="https://api.aigc369.com/v1")
    chain=ConversationChain(llm=model,memory=memory)

    response=chain.invoke({"input":prompt})
    return response["response"]

#memory=ConversationBufferMemory(return_messages=True)
#print(get_chat_response("牛顿提出过那些定律？",memory,os.environ["OPENAI_API_KEY2"]))
#print(get_chat_response("我的上一个问题是什么？",memory,os.environ["OPENAI_API_KEY2"]))