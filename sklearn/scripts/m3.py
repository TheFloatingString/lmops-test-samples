from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


def main():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=42
    )

    print(X_train.shape)
    print(X_test.shape)
    print(y_train.shape)
    print(y_test.shape)


if __name__ == "__main__":
    main()
