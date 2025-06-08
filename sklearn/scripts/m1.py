from sklearn.datasets import load_iris


def main():
    iris = load_iris()
    print(iris.data)


if __name__ == "__main__":
    main()
