# cook your dish here
def solve():
    no_of_movies, space = map(int, input().split())
    max_rating = 0
    for _ in range(no_of_movies):
        movie_space, movie_rating = map(int, input().split())
        if movie_space <= space:
            max_rating = max(max_rating, movie_rating)
    print(max_rating)

T = int(int(input()))
for _ in range(T):
    solve()
