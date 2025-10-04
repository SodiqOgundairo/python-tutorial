# xml can be used for a lot of things like storing data, configuration files, etc.
# it is a markup language that defines a set of rules for encoding documents in a format that
# it can be used for graphical user interfaces, data storage, and more.
# it is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.

# two ways to use XML is the
# SAX Is more memory-efficient as it only processes a small portion of the document at a time. Memory consumption does not significantly increase with document size.and provides read-only access

# and DOM Requires more memory as it loads the entire document into memory. This can be problematic for very large XML files. and provides access to modify data
import xml.sax
from xml.sax.xmlreader import AttributesImpl

# handler = xml.sax.ContentHandler()
# parser


class GroupHandler(xml.sax.ContentHandler):

    def startElement(self, name, attrs):
        # print(name)
        self.current = name
        if self.current == 'person':
            print("\n\n****PERSON****")
            print(f"ID: {attrs['id']}")

    def characters(self, content):
        if self.current == 'name':
            self.name = content
        elif self.current == 'age':
            self.age = content
        elif self.current == 'weight':
            self.weight = content
        elif self.current == 'height':
            self.height = content

    def endElement(self, name):
        if self.current == 'name':
            print(f'Name: {self.name}')
        elif self.current == 'age':
            print(f'Age: {self.age}')
        elif self.current == 'weight':
            print(f'Weight: {self.weight}')
        elif self.current == 'height':
            print(f'Height: {self.height}')
        self.current = ''


handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')
