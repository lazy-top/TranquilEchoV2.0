from langchain_core.messages import SystemMessage
from langchain.prompts import ChatPromptTemplate,SystemMessagePromptTemplate
from langchain.memory import ConversationBufferMemory
def define_personal_sys_prompt(ai_name:str,ai_type:str,user_name:str,user_detail:str):
    prompt = SystemMessagePromptTemplate.from_template("你是{ai_name}，一名{ai_type}，正在为{user_name}提供服务。{other}{user_detail}")
    prompt.format(ai_name=ai_name,ai_type=ai_type,user_name=user_name,other="请根据以下信息为用户提供心理支持和建议：",user_detail=user_detail)
    return prompt

def define_personal_chain(prompt:ChatPromptTemplate):

    return prompt


