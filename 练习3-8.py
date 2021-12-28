"""
方法.sort():按字母顺序永久性的改变列表元素顺序
函数sorted()：按字母顺序临时性的该表元素顺序,参数reverse=True
方法.reverse()：将列表元素顺序永久性的反转排列
函数len()：获取列表长度
"""

five_places = ['America','Taiwang','Xinjiang','Iceland','Shanghai']
print(five_places)

print(sorted(five_places))
print(five_places)

print(sorted(five_places,reverse=True))

print(five_places)

five_places.reverse()
print(five_places)

print("调用sort()方法")

# print(five_places.sort())
# print(five_places.sort(reverse=True))\

five_places.sort()
print(five_places)

five_places.sort(reverse=True)
print(five_places)


