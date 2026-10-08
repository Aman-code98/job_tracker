#     # Ask for a favorite color. Keep asking until the answer isn’t blank.
# # Ask for a size, accepting only small, medium, or large, so that " LARGE " also works.

# sizes = ['small', 'medium', 'large']
# size = input('what is  your Size? : ').strip().lower()

# while size not in sizes:
#     print('Invalid size. Please enter small, medium, or large.')
#     size = input('what is  your Size? : ').strip().lower()
# print(f' The size you have entered is {size}')


movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Forrest Gump"]

for movie in movies:
    print(movie)

people = [{'name': 'Aman', 'age': 27},
         {'name': 'Max', 'age': 30},
         {'name': 'John', 'age': 25}
         ]

for index, name in enumerate(people, start = 1):
    print(index , name['name'], name['age'])