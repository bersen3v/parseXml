from xml import xml
xml = xml.replace("<Запрос_x0020_средний_x0020_балл>","*")
xml = xml.replace("</Запрос_x0020_средний_x0020_балл>","*")
xml = xml.replace("*\n*","*")
xml = xml.replace("\n", "")
xml = xml.split("*")
xml.pop(0)
xml.pop(len(xml)-1)
# print(*xml, sep='\n')

print(xml)
# parsed_data = []

# for item in xml:
#     item_dict = {}
#     start = 0
#     while start < len(item):
#         start_tag = item.find('<', start)
#         end_tag = item.find('>', start)
#         print(start_tag, end_tag)
#         start+=1

# print(parsed_data)
    
