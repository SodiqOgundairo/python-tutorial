# read  content in xml_sax.py
import xml.dom.minidom

domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

# dunno why this eror though, but it works
persons = group.getElementsByTagName('person')

for person in persons:
    print('\n\n **** PERSON ****')
    if person.hasAttribute('id'):
        print(f'ID: {person.getAttribute('id')}')
    print(
        f'Name: {person.getElementsByTagName("name")[0].childNodes[0].nodeValue}')
    print(
        f'Age: {person.getElementsByTagName("age")[0].childNodes[0].nodeValue}')
    print(
        f'Weight: {person.getElementsByTagName("weight")[0].childNodes[0].nodeValue}')
    print(
        f'Height: {person.getElementsByTagName("height")[0].childNodes[0].nodeValue}')


# manipulating the xml data in my memory
persons[2].getElementsByTagName(
    'name')[0].childNodes[0].nodeValue = 'Yemi Ogundairo'
persons[0].setAttribute('id', '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = '-10'


# now sending the update to the xml file maybe create a new file instead of updating the old one
domtree.writexml(open('data2.xml', 'w'))


# creating  totally new element
newperson = domtree.createElement('person')
newperson.setAttribute('id', '6')

name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Tolulope Oguntimehin'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('30'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('70'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('150'))


newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open('data2.xml', 'w'))
