from xml import xml

def getXmlObjects(xml):
  xml = xml.replace("<Запрос_x0020_средний_x0020_балл>","*")
  xml = xml.replace("</Запрос_x0020_средний_x0020_балл>","*")
  xml = xml.replace("*\n*","*")
  xml = xml.replace("\n", "")
  xml = xml.split("*")
  xml.pop(0)
  xml.pop(len(xml)-1)
  return xml

def parseXmlFloor(data):
  users = []
  for object in data:
    user = {}
    while len(object) > 0:
      start, end= object.find("<"), object.find(">")
      key = object[start+1:end]
      object = object.replace(f"<{key}>", "").replace(f"</{key}>", "*").split("*")
      user[key] = object[0]
      object = object[-1]
    users.append(user)
  return users

def clear(s):
  s = s.replace(">","").replace("<","").replace("/","").split(" ")[0]
  return s

def show(users):
  for user in users:
      print('')
      for key in user.keys():
        print(f"{key}: {user[key]}")

def main():
  global xml
  xml = xml.splitlines()[1:]
  lastXml = xml
  while len(xml)>0:
    if(clear(xml[0]) == clear(xml[-1])):
        lastXml = xml
        xml = xml[1:-1]
    else:
      data = getXmlObjects("\n".join(lastXml))
      users = parseXmlFloor(data)
      show(users)
      xml = []

main()
    

    


  

    
    
      
