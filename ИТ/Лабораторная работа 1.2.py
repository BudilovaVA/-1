# TODO Найдите количество книг, которое можно разместить на дискете
v = 1.44*1024*1024
simv = 25
lines = 50
pages = 100
book = 4 * simv * lines * pages
books = v/book
print("Количество книг, помещающихся на дискету:", round (books))
