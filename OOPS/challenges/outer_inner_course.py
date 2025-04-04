class Course:
    def __init__(self, course_name, course_duration, *books ):
        self.course_name = course_name
        self.course_duration = course_duration
        self.books = [self.Book(title) for title in books]

    class Book:
        def __init__(self, title):
            self.title = title
        def __str__(self):
            return self.title

    def show_details(self):
        print(self.course_name)
        print(self.course_duration)
        print('Suggested Books: ')
        for b in self.books:
            print(b)

c = Course('CSE',4, 'DSA','DBMS','OS' )
c.show_details()