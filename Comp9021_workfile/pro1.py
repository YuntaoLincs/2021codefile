# 可以将英文输出为ASCII字符

map = {"A": "41", "B": "42", "C":"43","D":"44","E":"45","F":"46","G":"47","H":"48","I":"49","J":"4A","K":"4B","L":"4C","M":"4D","N":"4E","O":"4F","P":"50","Q":"51","R":"52","S":"53","T":"54","U":"55","V":"56","W":"57","X":"58","Y":"59","Z":"5A"," ":" "}
map1 = {value: key for key, value in map.items()}
map2 = map1.copy()
map2.update(map)  #暂时还没办法将ascii字符串输出为英文单词，只能将英文输出为ascii，需要解决读取字符问题
print(map2)
i = input("please enter the sentence:")
i_upper = i.upper()
print(i_upper)
output = []
for char in i_upper:
    output.append(map2[char])
print(output)

str = ""
print(str.join(output))

    