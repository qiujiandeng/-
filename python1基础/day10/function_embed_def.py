# function_embed_def.py
# 此示例示意函数嵌套定义

def fn_outer():
    print("fn_outer被调用")
    #此处能否创建新的函数并且调用呢?
    def fn_inner():
        print("fn_inner被调用!")
    fn_inner()
    fn_inner()
    print("fn_outer调用结束")

fn_outer()