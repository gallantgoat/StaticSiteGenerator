from enum import Enum

class TextType(Enum):
    NORMAL = 1
    BOLD = 2
    ITALIC = 3
    CODE = 4
    LINK = 5
    IMAGE = 6

class TextNode:
    def __init__(self, text, type, url=None):
        self.text = text
        self.type = type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.type == other.type and self.url == other.url
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.type.value}, {self.url})"