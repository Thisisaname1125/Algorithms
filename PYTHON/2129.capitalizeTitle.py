# NOTE(Kun, 20240311): 使用for循环修改局部变量不会影响列表的值，错误代码示例如下：
# title = "capitalIze tHe titLe"
# ls = title.split(" ")
# for stri in ls:
#     if len(stri) == 1 or len(stri) == 2:
#         stri = stri.lower()
#     else:
#         stri = stri.capitalize()
# print(" ".join(ls))

# NOTE(Kun, 20240311) 解法1：enumerate、
title = "capitalIze tHe titLe"
ls = title.split(" ")
for index, stri in enumerate(ls):
    if len(stri) == 1 or len(stri) == 2:
        ls[index] = ls[index].lower()
    else:
        ls[index] = ls[index].capitalize()
print(" ".join(ls))

# NOTE(Kun, 20240311) 解法2：新建列表/.
# title = "capitalIze tHe titLe"
# ls = title.split(" ")
# lsz = [stri.lower() if len(stri) == 1 or len(stri) == 2 else stri.capitalize() for stri in ls]
# print(" ".join(lsz))