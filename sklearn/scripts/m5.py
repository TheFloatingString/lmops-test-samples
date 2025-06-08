from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


def main():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.3, random_state=42
    )

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    print(clf.score(None, y_test))


if __name__ == "__main__":
    main()
