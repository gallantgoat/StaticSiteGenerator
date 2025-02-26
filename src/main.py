from textnode import TextNode, TextType

def main():
    main_node = TextNode("Help me!", TextType.BOLD, "https://www.google.com")
    print(main_node)

if __name__ == "__main__":
    main()