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
import pyttsx3 
engine = pyttsx3.init()
# 设置语速 (words per minute)
engine.setProperty('rate', 200)  # 语速为每分钟150个单词

# 设置音量 (0.0 到 1.0)
engine.setProperty('volume', 0.9)  # 音量为80%的最大音量

# 设置音高 (0.0 到 2.0, 1.0为默认值)
engine.setProperty('pitch', 1.2)  # 音高为默认值
print(engine.getProperty('voice'))

def say(text):
    engine.say(text)
    engine.save_to_file(text,"output.mp3")
    engine.runAndWait()


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

from langchain import hub
if __name__ == "__main__":
    say("您好，我是您的虚拟助手，有什么可以为您服务的呢？")
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
