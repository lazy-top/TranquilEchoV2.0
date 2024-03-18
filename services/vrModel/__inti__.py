import py360convert
from PIL import Image
import numpy as np
from pygltflib import GLTF2
from pygltflib.utils import Animation, Channel, Sampler, Node

#单张png图片转成高质量的360全景图
def imgto360():

    # 读取PNG图片
    input_image = np.array(Image.open('input.png'))

    # 将Equirectangular格式的图片转换成Cubemap格式
    cubemap_image = py360convert.e2c(input_image, face_w=1024, mode='bilinear', cube_format='dice')

    # 保存转换后的Cubemap格式图片
    Image.fromarray(cubemap_image).save('output_cubemap.png')

def glbRun():
    # 加载GLB模型
    filename = "your_model.glb"
    gltf = GLTF2().load(filename)

    # 创建一个新的动作
    animation = Animation()
    animation.name = "your_animation"

    # 创建动作的采样器
    sampler = Sampler()
    sampler.input = 0  # 输入时间
    sampler.output = 1  # 输出动作值
    animation.samplers.append(sampler)

    # 创建动作的通道
    channel = Channel()
    channel.sampler = 0  # 使用第一个采样器
    channel.target.node = 0  # 目标节点索引
    channel.target.path = "translation"  # 动作类型（平移、旋转等）
    animation.channels.append(channel)

    # 将新动作添加到GLB模型中
    gltf.animations.append(animation)

    # 保存更新后的GLB模型
    filename2 = "updated_model.glb"
    gltf.save(filename2)