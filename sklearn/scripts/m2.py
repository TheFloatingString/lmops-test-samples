from sklearn.datasets import load_iris


def main():
    iris = load_iris()
    print(iris.feature_names)
    print(iris.target_names)
    # print(iris.data)


if __name__ == "__main__":
    main()
