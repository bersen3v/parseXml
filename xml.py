# <root>
#   <user>
#     <info>
#       <metadata>
#         <id>1<id>
#         <regdate>18.11.2023<regdate>
#       <metadata>
#       <firstname>Иван</firstname>
#       <lastname>Берсенев</lastname>
#     </info>
#     <role>студент</role>
#   </user>
#   <user>
#     <info>
#       <firstname>Иван</firstname>
#       <lastname>Берсенев</lastname>
#     </info>
#     <role>студент</role>
#   </user>
#   <user>
#     <info>
#       <firstname>Иван</firstname>
#       <lastname>Берсенев</lastname>
#     </info>
#     <role>студент</role>
#   </user>
# </root>


xml = """
<root>
<user1>
<info>
<metadata>
<id>
1
</id>
<regdate>
18.11.2023
</regdate>
</metadata>
<firstname>
<realname>
Иван
</realname>
</firstname>
<lastname>
Берсенев
</lastname>
</info>
<role>
студент
</role>
</user1>
<user2>
<info>
<firstname>
Иван
</firstname>
<lastname>
Берсенев
</lastname>
</info>
<role>
студент
</role>
</user2>
</root>
"""
