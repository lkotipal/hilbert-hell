import numpy as np

def rotate(n, d):
    return leftRotate(n, d) if d > 0 else rightRotate(n, -d)

def leftRotate(n, d):
    return ((n << d) % (1 << 3))|(n >> (3 - d))

def rightRotate(n, d):
    return (n >> d)|(n << (3 - d)) & 0b111

''' "Butz", from Lawder
Y = [
    0b000,
    0b001,
    0b010,
    0b011,
    0b100,
    0b101,
    0b110,
    0b111
]

X_1 = [
    0b000,
    0b001,
    0b011,
    0b010,
    0b110,
    0b111,
    0b101,
    0b100
]

X_2 = [
    (0b000, 0b001),
    (0b000, 0b010),
    (0b000, 0b010),
    (0b011, 0b111),
    (0b011, 0b111),
    (0b110, 0b100),
    (0b110, 0b100),
    (0b101, 0b100)
]
'''

X_1 = [
    0b000,
    0b001,
    0b011,
    0b010,
    0b110,
    0b111,
    0b101,
    0b100
]

X_2 = [
    (0b000, 0b001),
    (0b000, 0b010),
    (0b000, 0b010),
    (0b011, 0b111),
    (0b011, 0b111),
    (0b110, 0b100),
    (0b110, 0b100),
    (0b101, 0b100)
]

dYdict = {
    4: 0, 
    2: 1, 
    1: 2
}

leftShiftDict = {
    0: [0, 1, 2],
    1: [1, 2, 0],
    2: [2, 0, 1],
}

dY = list([i ^ j for i, j in X_2])
TY = [(i[0], dYdict[j]) for i, j in zip(X_2, dY)]
print(TY)

#TY = [np.stack((i, i[[2, 0, 1]], i[[1, 2, 0]])) for i in dY]
#
#for i in range(8):
#    t = np.zeros((3, 3))
#    for j in range(3):
#        t[j, j] = -1 if X_2[i][0][j] else 1
#    TY[i] = np.dot(t, TY[i])

X1 = [[-1 for i in range(8)]]
for i, X_i in enumerate(X_1):
    X1[0][i] = X_i

state = 0
states = {}
tm = [[-1 for i in range(8)]]
for i, T in enumerate(TY):
    for j, mat in states.items():
        if (T[1] == mat[1] and np.array_equal(T[0], mat[0])):
            tm[0][i] = j
            break
    else:
        state = state + 1
        states[state] = T
        tm[0][i] = state

u = 1
while u <= state:
    X1.append([-1 for i in range(8)])
    tm.append([-1 for i in range(8)])
    X2u, dYu = states[u]
    for i in range(8):
        j = leftRotate(i ^ states[u][0], states[u][1])
        p = X1[0].index(j)
        X1[u][p] = i
        X2q, dYq = states[tm[0][p]]
        TM = (rightRotate(X2q, dYu) ^ X2u, (dYq + dYu) % 3)
        for idx, mat in states.items():
            if (TM[1] == mat[1] and np.array_equal(TM[0], mat[0])):
                tm[u][p] = idx
                break
        else:
            state = state + 1
            states[state] = TM
            tm[u][p] = state
    u = u + 1

print('X1')
for i in X1:
    for j in i:
        print(j, end=', ')
    print()

print('\ntm')
for i in tm:
    for j in i:
        print(j, end=', ')
    print()