
# exercize_3:
#     有一个集合:
#     s = {'唐僧','悟空','八戒','沙僧'}
#     用for语句来遍历所有元素如下:
#     for x  in s :
#         print(x)
#     else:
#         print("变量结束")
#     请将上面的for语句改成while和语句迭代器实现

s = {'唐僧','悟空','八戒','沙僧'}
it = iter(s)
i = 0

while True:
    try:
        print(next(it))
    except StopIteration:
        print("遍历结束")
        break

