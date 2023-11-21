import json
import xml.etree.ElementTree as ET

class Shop:        
    def __init__(self, category, name, price):
        self.category = category         
        if name == "":           
            raise NameException        
        self.name = name
        if price < 0:            
            raise ValueError("error") 
        self.price = price

    def __todict__(self):
        js = {"Type": type(self).__name__}
        for key, value in vars(self).items():
            js[key] = str(value)
        return js


class NameException(Exception):
    def str(self):                
        return "Name missing"


class Product(Shop):    
    def __init__(self, category, name, price, quantity):        
        super().__init__(category, name, price)        
        self.quantity = quantity
    
class Service(Shop):    
    def __init__(self, category, name, price, duration):        
        super().__init__(category, name, price)        
        self.duration = duration



def read_json(filename: str):
    with open(filename, "r") as file:
        text = file.read()
        return json.loads(text)
def write_json(filename: str, items):
    with open(filename, "w") as my_file:
        my_file.write(json.dumps(items))

def read_xml(filename: str): 
    result = []
    tree = ET.parse(filename)
    root = tree.getroot()
    for items in root:
        element = dict()
        for item in items:
            element[item.tag] = item.text
        result.append(element)
    return result

def write_xml(elements, filename): 
    root = ET.Element('root')
    for element in elements:
        item = ET.SubElement(root, 'item')
        for key, value in element.items():
            ET.SubElement(item, key).text = element[key]
            tree = ET.ElementTree(root)
            tree.write(filename)

product = Product("meat", "chicken", 200, 50)
write_json("out.json", product.__todict__())
print(read_json("out.json"))

shop = [product.__todict__(), Service("gift", "sertificate", 1000, 10).__todict__()]
write_xml(shop, "out.xml")
print(read_xml("out.xml"))
