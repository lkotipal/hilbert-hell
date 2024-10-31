import numpy as np

def rotate(n, d):
    return leftRotate(n, d) if d > 0 else rightRotate(n, -d)

def leftRotate(n, d):
    return ((n << d) % (1 << 3))|(n >> (3 - d))

def rightRotate(n, d):
    return (n >> d)|(n << (3 - d)) & 0b111

def toVector(i):
    return np.array([i & 4 > 0, i & 2 > 0, i & 1 > 0], int)

def toBinary(v):
    return v[0] * 4 + v[1] * 2 + v[2]

def leftMatmul(v, M):
    ret = np.array([0, 0, 0], int)
    for i, row in enumerate(M):
        for j, elem in enumerate(row):
            if elem > 0:
                ret[j] = toVector(v)[i]
            elif elem < 0:
                ret[j] = not toVector(v)[i]
    return toBinary(ret)

def rightMatmul(v, M):
    ret = np.array([0, 0, 0], int)
    for i, row in enumerate(M):
        for j, elem in enumerate(row):
            if elem > 0:
                ret[i] = toVector(v)[j]
            elif elem < 0:
                ret[i] = not toVector(v)[j]
    return toBinary(ret)

''' This table is just indexing 0 - 7
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
'''

''' "Butz", from Lawder
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

#''' "Butz", from Haverkort
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
#'''

dYdict = {
    4: 0, 
    2: 1, 
    1: 2
}

dY = list([i ^ j for i, j in X_2])

handedness = np.array([False for _ in range(8)]) # 'Butz'
handedness[[1, 4, 5]] = True # 'alfa' from Haverkort

TY = [np.stack((toVector(i), toVector(leftRotate(i, 1) if flip else rightRotate(i, 1)), toVector(leftRotate(i, 2) if flip else rightRotate(i, 2)))) for i, flip in zip(dY, handedness)]

for i in range(8):
    t = np.zeros((3, 3), int)
    for j in range(3):
        t[j, j] = -1 if X_2[i][0] & (4 >> j) else 1
    TY[i] = np.dot(TY[i], t)

X1 = [[-1 for _ in range(8)]]
for i, X_i in enumerate(X_1):
    X1[0][i] = X_i


state = 0
states = {0: np.identity(3, int)}
tm = [[-1 for _ in range(8)]]
for i, T in enumerate(TY):
    for j, mat in states.items():
        if (np.array_equal(T, mat)):
            tm[0][i] = j
            break
    else:
        state = state + 1
        states[state] = T
        tm[0][i] = state

u = 1
while u <= state:
    X1.append([-1 for _ in range(8)])
    tm.append([-1 for _ in range(8)])
    TMu = states[u]
    for i in range(8):
        j = rightMatmul(i, TMu)
        p = X1[0].index(j)
        X1[u][p] = i
        TMq = states[tm[0][p]]
        TMw = np.dot(TMq, TMu)
        for idx, mat in states.items():
            if (np.array_equal(TMw, mat)):
                tm[u][p] = idx
                break
        else:
            state = state + 1
            states[state] = TMw
            tm[u][p] = state
    u = u + 1

X1_inv = []
tm_inv = []
for u, (X1u, tmu) in enumerate(zip(X1, tm)):
    X1_inv.append([-1 for _ in range(8)])
    tm_inv.append([-1 for _ in range(8)])
    for idx, (x1, state) in enumerate(zip(X1u, tmu)):
        X1_inv[u][x1] = idx
        tm_inv[u][x1] = state

contents = ''
print('static unsigned const data3d [] = {')
for i in X1:
    for j in i:
        contents += f'{j}, '
    contents += '\n'
print(f'{contents[:-3]}\n}};\n')

contents = ''
print('static unsigned const state3d [] = {')
for i in tm:
    for j in i:
        contents += f'{j}, '
    contents += '\n'
print(f'{contents[:-3]}\n}};\n')

contents = ''
print('static unsigned const idata3d [] = {')
for i in X1_inv:
    for j in i:
        contents += f'{j}, '
    contents += '\n'
print(f'{contents[:-3]}\n}};\n')

contents = ''
print('static unsigned const istate3d [] = {')
for i in tm_inv:
    for j in i:
        contents += f'{j}, '
    contents += '\n'
print(f'{contents[:-3]}\n}};\n')