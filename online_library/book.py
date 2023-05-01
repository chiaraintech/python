class Book():
    def __init__(self, id, title, content, last_page):
        self.id = id
        self.title = title
        self.content = content
        self.last_page = 0
    
    def display_page(self, last_page):
        return self.content[self.last_page]
    
    def turn_page(self, last_page):
        self.last_page += 1
        return self.display_page(last_page)