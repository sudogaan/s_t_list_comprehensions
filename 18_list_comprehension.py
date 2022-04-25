# list comprehensions: [expr for val in collection if test1 and test2]

squares = []

for i in range(1, 101):
	squares.append(i**2)
print(squares)

squares2 = [i**2 for i in range(1, 101)]
print(squares2)

remainders = [x**2 % 5 for x in range(1, 101)]
print(remainders)

movies = ["Star Wars", "Dune", "Casablanca", "Toy Story"]

gmovies = []
for title in movies:
	if title.startswith("G"):
	gmovies.append(title)
print(gmovies)

gmovies = [title for title in movies if title.startswith("G")]

movies = [("Citizen Kane", 1941), ("No Country for Old Men", 2007), ("The Lord of the Rings", 2001), ("Raiders of the Lost Ark", 1981)]

nmovies = []
for movie,year in movies:
	if year < 2000:
	nmovies.insert(movie)
print(nmovies)


nmovies = [movie for (movie,year) in movies if year < 2000]


v = [2, -3, 1]
# for multiplication

w = [4*x for x in v]
print(w)


#cartesian product
# if A and B are sets, then the cartesian product is the set of pairs(a,b) where "a" is in A and "b" is in B.
# example
#A = {1, 3}
#B = {x, y}
# A x B = {(1, x), (1, y), (3, x), (3, y)}

A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(a, b) for a in A for b in B]
print(cartesian_product)




