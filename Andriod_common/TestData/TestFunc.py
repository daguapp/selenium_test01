# 首先定义一个普通的函数
def print_text(name):
    return 'hello,' + name


# 再定义一个嵌套函数，分别以函数和普通的字符串作为参数
def add_tag(func):
    def prt_func(name):
        return '<p>{0}</p>'.format(func(name))

    return prt_func

lista=[2,61,12,4,5,321,424,556,4231]
count=0
for i in range(len(lista)):
    for x in range(len(lista)-i-1):
        count+=1
        if lista[x]> lista[x+1]:
            lista[x],lista[x+1]=lista[x+1],lista[x]
print(lista)
print(f"执行运算：{count}")

# def bubble_sort(li):
#     for i in range(len(li)):
#         for x in range(len(li)-1):
#             if li[x] > li[x+1]:
#                 li[x],li[x+1]=li[x+1],li[x]
#     return li
# print(bubble_sort(lista))
class  TestB:
    def __setattr__(self, key, value):
        print("这是一条测试")

t=TestB()
t.__setattr__()