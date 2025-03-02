from textnode import TextNode

def main():
    textnode = TextNode("This is some anchor text", TextNode.LINK, "https://www.boot.dev")
    print(textnode)

main()
