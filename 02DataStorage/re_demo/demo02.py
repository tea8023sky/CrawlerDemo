
import re



# 转义字符和原生字符串：


# 不用原生字符串，则需要4个 \  因为 python中 "\\n" = \n， 正则表达式中  "\\n" = \n，所以 "\\\\m" =>  \n
text = "apple \c"
ret = re.search('\\\\c',text)
print(ret.group())



# 原生字符串 r = raw = 原生的
# text = "apple \c"
# ret = re.search(r'\\c',text)  # 相当于这层pyhton不会将字符进行转义，只有正则表达式的转义，所以 =》 \c
# print(ret.group())

