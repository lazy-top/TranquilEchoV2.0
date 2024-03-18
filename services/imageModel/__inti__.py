import requests
from bs4 import BeautifulSoup
import time
import os
from urllib.robotparser import RobotFileParser

def get_all_urls(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    # 尊重网站的Robots协议
    robots_url = url + '/robots.txt'
    response = requests.get(robots_url, headers=headers)
    if 'Disallow' in response.text:
        print("该网站禁止爬取")
        return
    
    try:
        # 模拟浏览器发送请求
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"请求失败：{e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    # 解析页面内容
    for link in soup.find_all('a'):
        href = link.get('href')
        img_name = ''
        # 获取href中间的后的‘/image/’后的全面内容
        if href and href.startswith('/image/'):
            img_name = href.split('/')[2]
            print(img_name)
        # 获取图片
        img_link = link.find('img')
        if img_link:
            img_url = img_link.get('src')
            if not img_url.startswith('http'):
                img_url = url + img_url
            print(img_url)
            # 获取img_url内容里面的jpeg后的?h=xx&q=xx参数
            height, width = '', ''
            if '?h=' in img_url:
                height = img_url.split('?h=')[-1].split('&')[0]
            if '&q=' in img_url:
                width = img_url.split('&q=')[-1]
            print(height, width)
            # 下载图片，控制请求速度
            try:
                download_image(img_url, headers=headers, img_name=img_name+'_'+height+'_'+width+'.jpeg')
            except requests.exceptions.RequestException as e:
                print(f"下载失败：{e}")

def download_image(img_url, headers, img_name):
    # 创建保存图片的目录
    dir_path = 'images'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    
    file_path = os.path.join(dir_path, img_name)
    # 发送请求获取图片内容
    response = requests.get(img_url, headers=headers, stream=True)
    response.raise_for_status()
    
    with open(file_path, 'wb') as f:
        for chunk in response.iter_content(1024):
            if chunk:
                f.write(chunk)
                
    print(f"图片 {img_name} 已保存。")

if __name__ == '__main__':
    get_all_urls('https://pixexid.com/search/360-panoramic')