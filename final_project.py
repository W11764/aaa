#coding:utf-8
"""
程序目标：对《黎明破晓的街道》文本中人物关系的提取，并利用Gelphi软件对人物关系可视化，生成人物关系图谱
作者：王娅文
"""

import codecs
import jieba.posseg as pseg
import jieba

names = {}
relationships = {}
lineNames = []

jieba.load_userdict("names.txt")
with codecs.open("黎明破晓的街道.txt", 'r','utf-8') as f:
    for line in f.readlines():
        poss = pseg.cut(line)  
        lineNames.append([])  
        for i in poss:
            if i.flag != 'nr' or len(i.word) < 2:
                continue  
            lineNames[-1].append(i.word)  
            if names.get(i.word) is None:  
                names[i.word] = 0
                relationships[i.word] = {}
            names[i.word] += 1

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1

with codecs.open("node.txt", "w", "utf-8") as f:
    f.write("ID Label Weight\r\n")
    for name, times in names.items():
        p = ['小姐','老公公','明白','东白乐','平安夜','滑雪','阿姨','宣言','仲西家','威士忌','红茶','阿嬷','封印','道德','温泉','高中生','白发 ','徐缓','藉口','老公','欧吉桑','高圆寺','富豪','时髦','高尔夫球','谢谢','原谅','浅笑','令尊','白发','顾忌','仲西']
        if name in p:
            continue
        if times > 3:
            f.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("edge.txt", "w", "utf-8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for m, n in edges.items():
            if n > 3:
                f.write(name + " " + m + " " + str(n) + "\r\n")

f1 = open('edge.txt','r',encoding='utf-8')
f2=open('names.txt','r',encoding='utf-8').read()
lines=f1.readlines()
f1.close
A = []
t = ['Source','Target','Weight','秋叶','新谷','黑泽','古琦','渡部','有美子','园美','丽子','野田','芦原','真穗','尾崎','妙子','里村','加岛','绫子','达彦','钉宫真纪子','英惠','绘理','阿俊']
for line in lines:
    A.append([])
    m=line.strip('\n').split(' ')
    for x in m:
        A[-1].append(x)
for q in A:
    if q[0]and q[1] not in f2:
	    del(q)
f.close()
print(A)
