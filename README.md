1. Book.objects.filter(title__contains=('Django'))

2. Book.objects.filter(tag='Fiction')

3. Author.objects.filter(book__title__contains=('Django'))