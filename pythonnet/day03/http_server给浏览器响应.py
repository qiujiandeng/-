'''
http server v1.0
接收浏览器请求
返回固定的响应内容
'''
from socket import *
#函数封装 处理客户端请求(浏览器请求)
def handleClient(connfd):
    print('Request from',connfd.getpeername())
    request = connfd.recv(4096)#接收http请求
    #将request按行分割
    request_lines = request.splitlines()
    for line in request_lines:
        print(line)
    try:
        f = open('index.html')
    except IOError:
        response = 'HTTP/1.1 404 Not Found\r\n'
        response +='\r\n'
        response +='===Sorry not found ===='
    else:
        response = 'HTTP/1.1 200 OK\r\n'
        response +='\r\n'
        response += f.read()
    finally:
        #将结果发送给浏览器
        connfd.send(response.encode())


#main函数创建tcp套接字
def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(('0.0.0.0',8002))
    sockfd.listen(3)
    print("Listen to the port 8000")
    while True:
        connfd,addr = sockfd.accept()
        handleClient(connfd)  #用封装的函数负责具体请求处理
        connfd.close()

if __name__ == '__main__':
    main()
