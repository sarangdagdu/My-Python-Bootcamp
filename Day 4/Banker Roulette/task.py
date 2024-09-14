import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
# Traditional way
payer = random.randint(0,len(friends) - 1)
#Python way
cho = random.choice(friends)

print(f"Lucky Payer for tonight is {friends[payer]}")

print(f"Lucky Payer for tonight is {cho}")
