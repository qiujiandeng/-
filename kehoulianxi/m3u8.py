#!/usr/bin/env/python
#_*_coding:utf-8_*_
#Data:17-10-08
#Auther:苏莫
#Link:http://blog.csdn.net/lingluofengzang
#PythonVersion:python2.7
#filename:download_movie.py
 
import os
import sys
import requests
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
# 功能：爬取m3u8格式的视频
 
# 检查存储路径是否正常
def check_path(_path):
  # 判断存储路径是否存在
  if os.path.isdir(_path) or os.path.isabs(_path):
    # 判断存储路径是否为空
    if not os.listdir(_path):
      return _path
 
    else:
 
      print u'>>>[-] 目标文件不为空，将清空目标文件，是否更换路径？'
      flag = raw_input('>>>[*] Yes:1 No:2 \n>>>[+] [2]')
 
      try:
        if flag == '1':
          _path = raw_input(unicode('>>>[+] 请输入目标文件路径。\n>>>[+] ').encode('gbk'))
          check_path(_path)
        else:
          # 清空存储路径
          os.system('rd /S /Q ' + _path)
          os.system('mkdir ' + _path)
          return _path
      except Exception as e:
        print e
        exit(0)
 
  else:
    os.makedirs(_path)
    return _path
 
# 获取ts视频的爬取位置
def get_url(_url, _path):
 
  all_url = _url.split('/')
  url_pre = '/'.join(all_url[:-1]) + '/'
  url_next = all_url[-1]
 
  os.chdir(_path)
  # 获取m3u8文件
  m3u8_txt = requests.get(_url, headers = {'Connection':'close'})
  with open(url_next, 'wb') as m3u8_content:
    m3u8_content.write(m3u8_txt.content)
  # 提取ts视频的url
  movies_url = []
  _urls = open(url_next, 'rb')
  for line in _urls.readlines():
    if '.ts' in line:
      movies_url.append(url_pre + line[:-1])
    else:
      continue
 
  _urls.close()
  return movies_url
 
# 爬取ts视频
def download_movie(movie_url, _path):
  os.chdir(_path)
  print '>>>[+] downloading...'
  print '-' * 60
  error_get = []
 
  for _url in movie_url:
    # ts视频的名称
    movie_name = _url.split('/')[-1][-6:]
 
    try:
      # 'Connection':'close' 防止请求端口占用
      # timeout=30  防止请求时间超长连接
      movie = requests.get(_url, headers = {'Connection':'close'}, timeout=60)
      with open(movie_name, 'wb') as movie_content:
        movie_content.writelines(movie)
      print '>>>[+] File ' + movie_name + ' done'
    # 捕获异常，记录失败请求
    except:
      error_get.append(_url)
      continue
  # 如果没有不成功的请求就结束
  if error_get:
    print u'共有%d个请求失败' % len(file_list)
    print '-' * 60
    download_movie(error_get, _path)
  else:
    print '>>>[+] Download successfully!!!'
 
if __name__ == '__main__':
  try:
 
    _url = raw_input(unicode('>>>[+] 请输入指定的[.m3u8]目标URL。\n>>>[+] ').encode('gbk'))
    _path = raw_input(unicode('>>>[+] 请输入存储目标文件路径。\n>>>[+] ').encode('gbk'))
 
    storage_path = check_path(_path)
    movie_url = get_url(_url, storage_path)
    download_movie(movie_url, storage_path)
 
  except Exception as e:
    print e