from factory.factory1 import ConcreteFactory1
from factory.factory2 import ConcreteFactory2
from control.runner import code

if __name__ == "__main__":
    f1 = ConcreteFactory1()
    code(f1)

    f2 = ConcreteFactory2()
    code(f2)