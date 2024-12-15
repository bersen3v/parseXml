from xml import xml

xml = xml.splitlines()
xml.pop(0)

stack = []
answer = {}

def clear(tag):
  answer = ''
  for char in tag:
    if(char not in ['<','>','/']):
      answer+=char
  return answer

def isTag(row):
  return ">" in row

def paste(data):
  curr = answer
  for i in stack:
    if(i in curr):
      curr[i]=curr[i]
    else:
      curr[i] = {}
    curr = curr[i]
  curr['value'] = data

for row in xml:
  if(isTag(row)):
    tag = clear(row)
    if(stack!=[] and stack[-1]==tag):
      stack.pop(len(stack)-1)
    else:
      stack.append(tag)
  else:
    paste(row)

print(answer)


json = {
  'root': {
    'user1': {
      'info': {
        'metadata': {
          'id': {'value': '1'}, 
          'regdate': {'value': '18.11.2023'}}, 
        'firstname': {'value': 'Иван'}, 
        'lastname': {'value': 'Берсенев'}}, 
        'role': {'value': 'студент'}
    }, 
    'user2': {
      'info': {
        'firstname': {'value': 'Иван'}, 
        'lastname': {'value': 'Берсенев'}}, 
        'role': {'value': 'студент'}
    }
  }
}