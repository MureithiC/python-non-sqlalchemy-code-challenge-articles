class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not (5 <= len(title) <= 50):
            raise ValueError("Title length must be between 5 and 50 characters inclusive")
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise TypeError("magazine must be an instance of Magazine")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)
        if author not in magazine._contributors:
            magazine._contributors.append(author)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Title attribute is immutable")

    @title.deleter
    def title(self):
        raise AttributeError("Title attribute cannot be deleted")


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Cannot modify the name attribute")

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def topic_areas(self):
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters inclusive")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []
        self._contributors = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("article must be an instance of Article")
        self._articles.append(article)
        if article.author not in self._contributors:
            self._contributors.append(article.author)

    def articles(self):
        return self._articles

    def contributors(self):
        return self._contributors

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return [author for author in self._contributors if sum(1 for article in self._articles if article.author == author) > 2]
