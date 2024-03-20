# from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
# import os
# from dotenv import load_dotenv
# from fastapi import HTTPException
# from langchain import hub
# from langchain.memory import ConversationBufferMemory
# from langchain.agents import AgentExecutor, create_structured_chat_agent
# from services.langchain.Tools import Knowledge_search
# from services.langchain.Knowledge import load_pdf_texts,create_knowledge_base
# load_dotenv()

# qianfan_apikey = os.getenv("QIANFAN_AK")
# qianfan_scretkey = os.getenv("QIANFAN_SK")
# os.environ["QIANFAN_AK"] = qianfan_apikey
# os.environ["QIANFAN_SK"] = qianfan_scretkey
# def getqf()->QianfanLLMEndpoint:
#     QianfanLLM= QianfanLLMEndpoint(streaming=True,
#                                 model="ERNIE-Bot-turbo",)
#     return QianfanLLM
# import pyttsx3 
# engine = pyttsx3.init()
# # 设置语速 (words per minute)
# engine.setProperty('rate', 200)  # 语速为每分钟150个单词

# # 设置音量 (0.0 到 1.0)
# engine.setProperty('volume', 0.9)  # 音量为80%的最大音量

# # 设置音高 (0.0 到 2.0, 1.0为默认值)
# engine.setProperty('pitch', 1.2)  # 音高为默认值
# print(engine.getProperty('voice'))

# def say(text):
#     engine.say(text)
#     engine.save_to_file(text,"output.mp3")
#     engine.runAndWait()


# def imgto360():

#     # 读取PNG图像
#     e_img = np.array(Image.open('input.png'))

#     # 将equirectangular图像转换成cubemap
#     cube_h = py360convert.e2c(e_img, face_w=256, mode='bilinear', cube_format='dice')

#     # 将cubemap转换成equirectangular
#     equirectangular_img = py360convert.c2e(cube_h, h=1024, w=2048, cube_format='dice')

#     # 保存equirectangular图像
#     Image.fromarray(equirectangular_img).save('output.jpg')
        
# import bpy
# from services.langchain.Knowledge import  load_pdf_texts,create_pdf_knowledge_base


# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:19
#聊天功能实现
# @File    : ChatService.py
# @Software: PyCharm

# import asyncio

"""
CRISPE Prompt Framework提示词模板:
能力与角色: 请输入你希望大模型扮演怎样的角色。

背景信息: 请输入背景信息和上下文。

指令: 请输入你希望大模型具体执行的任务。

输出风格: 请输入期望大模型生成内容的风格。 例如：我希望你能以详细且专业的方式回答我

输出范围： 请输入期望大模型生成内容的风格。

"""
# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 11:19
#聊天功能实现
# @File    : ChatService.py
# @Software: PyCharm

# import asyncio
from langchain import hub
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor,agent
from services.langchain.Models import getqf
from services.langchain.Tools import Knowledge_search
from langchain.prompts import PromptTemplate
chat_history =ConversationBufferMemory()

AgentExecutor
def chat_service(text: str):
    prompt = PromptTemplate(input_variables=['chat_history', 'input'] ,
                                template=
    """Assistant是由OpenAI训练的大型语言模型，现在以小海的身份出现，小海是一位专注的心理咨询师。

    小海旨在协助完成广泛的任务，特别是为心理健康领域提供支持和指导。作为咨询师，小海能够参与富有同情心的对话，提供与情感和心理问题相关的连贯且相关的回应。

    作为心理咨询师，小海致力于：
    1. **建立信任**：与客户建立信任关系，耐心倾听并理解他们的感受和经历，确保他们感到被接纳和理解。
    2. **使用开放式问题**：鼓励客户分享超出简单“是”或“否”答案的信息。例如，“您能告诉我更多关于您的感受吗？”或“您对这件事有什么看法？”
    3. **倾听**：积极倾听客户，不打断他们，为他们提供充足的时间和空间来表达自己。
    4. **提供反馈**：在客户分享他们的感受和经历后，提供反馈，确认他们的情绪，并让他们知道他们被理解。例如，“我听到您感到相当沮丧，这让我认为您可能正在经历一些困难。”
    5. **提出建议**：在适当的时候，小海可以提出策略帮助客户解决问题，这些建议应基于客户的具体情况和需求，而不是咨询师的个人观点或期望。
    6. **保持尊重**：在咨询过程中，无论客户的观点如何，或者他们是否同意咨询师的建议，都要尊重客户。
    7. **保持专业**：保持专业态度，避免与客户建立过于亲密的关系，以防止潜在的滥用或依赖。
    8. **提供支持**：提供持续的支持，帮助客户应对挑战和困难，可能包括提供资源，如书籍、文章或其他信息，或在必要时推荐寻求其他形式的帮助。

    总之，小海是一名专业又温馨的心理咨询师，提供一个富有同情心的耳朵和深思熟虑的指导，帮助解决任何的问题。

    最终答案：[您的回答在这里]'
    开始！
    以前的对话记录：{chat_history}

    新输入: {input}
    """)
    qfModel=getqf()
    prompt=prompt.format(chat_history=chat_history,input=text)
    print(prompt)
    res=qfModel.invoke(prompt)
    chat_history.chat_memory.add_user_message(text)
    chat_history.chat_memory.add_ai_message(res)
    print(res)
    return res






        



if __name__ == "__main__":
    chat_service("你好,我头有点痛，是为什么呢？")




    # say("您好，我是您的虚拟助手，有什么可以为您服务的呢？")
    # create_pdf_knowledge_base(load_pdf_texts("./resouces/pdf"),'test')
   



    # 假设你已经导入了glb文件，并且知道物体的名称
    # object_name = "你的物体名称"
    # obj = bpy.data.objects[object_name]

    # # 确保物体被选中和激活
    # bpy.context.view_layer.objects.active = obj
    # obj.select_set(True)

    # # 创建或获取动画数据
    # if obj.animation_data is None:
    #     obj.animation_data_create()
    # action = bpy.data.actions.new(name="MyAction")
    # obj.animation_data.action = action

    # # 在第1帧和第30帧设置位置关键帧
    # obj.location = (0, 0, 0)
    # obj.keyframe_insert(data_path="location", frame=1)
    # obj.location = (5, 5, 5)
    # obj.keyframe_insert(data_path="location", frame=30)

# 播放动画（在Blender UI中手动操作）



    # imgto360()

    # QianfanLLM=getqf()
    # prompt = hub.pull("hwchase17/structured-chat-agent")
    # memory = ConversationBufferMemory(memory_key="chat_history")
    # tools=[
    #     Knowledge_search
    # ]
    # qfModel=getqf()
    # agent = create_structured_chat_agent(qfModel, tools, prompt)
    # agent_executor = AgentExecutor(
    #     agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
    # )


    # for chunk in QianfanLLM.stream("你是谁呢？"):
    #   print(chunk)
    # texts=load_pdf_texts("./resouces/pdf")
    # print(texts)
    # knowledge_base = create_knowledge_base(texts)

#单张png图片转成高质量的360全景图
