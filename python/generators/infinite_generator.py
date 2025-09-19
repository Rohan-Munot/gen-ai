def infinite_generator():
    count = 1
    while True:
        yield f"Count: {count}"
        count += 1

infinite = infinite_generator()
for _ in range(4,11):
    print(next(infinite))