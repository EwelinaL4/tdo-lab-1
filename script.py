import os

name = os.getenv("MY_NAME", "Unknown user")

print(f"Hello {name}!")
print("This Python script is using an environment variable from GitHub Actions.")
