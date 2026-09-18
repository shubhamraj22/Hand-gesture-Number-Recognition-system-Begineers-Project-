import sys
import numpy as np
import pandas as pd
from random import randint
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

print("Treinando...")
# leitura dados de treino
train = pd.read_csv("train.csv").to_numpy()
# cria a arvore de decisao
clf = DecisionTreeClassifier()

#treino
value_train = train[0:, 1:]
label_train = train[0:, 0]
clf.fit(value_train, label_train)

if len(sys.argv) <= 1:

    # leitura dos dados de teste
    test = pd.read_csv("test.csv").to_numpy()

    #teste
    value_test = test[0:, 0:]
    predict = clf.predict(value_test)

    for count in range(5):
        i = randint(0,len(value_test)-1)
        num = value_test[i]
        num.shape = (28, 28)
        plt.figure(i)
        plt.imshow(255-num, cmap='gray')
        plt.show()
        print("predict value: {}".format(predict[i]))

else:
    # leitura do dado passado por argumento
    img = abs((imageio.imread(sys.argv[1], as_gray=True))-255)
    img = np.array(img).flatten()
    pd.DataFrame(img).to_csv("image.csv")

    img = pd.read_csv("image.csv").as_matrix()

    value = img[0:, 1]
    value = value.reshape(1, -1)
    predict = clf.predict(value.reshape(1, -1))

    num = value
    num.shape = ([28, 28])
    plt.figure(sys.argv[1])
    plt.imshow(255-num, cmap='gray')
    plt.show()
    print("predict value: {}".format(predict))
