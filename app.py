def hello():
    return "Hello from my first CI/CD pipeline"


if __name__ == "__master__":
    print(hello())
