import numpy as np

def main():
    list1, list2 = [1,2,3], [4,5,6]
    a, b = np.array(list1), np.array(list2)

    c = a + b
    d = a - b
    e = a * b
    f = a / b
    print(c, d, e, f)
    g = a * 2
    h = b + 2
    print(g, h)
    print('a 자료형 : ', type(a), type(a[0]))
    print('a의 shape : ', a.shape)
    print('a의 차원 : ', a.ndim)
    print('a의 크기 : ', a.size)
    print('a의 데이터 : ', a)


if __name__=="__main__":
    main()
