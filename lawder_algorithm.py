from dataclasses import asdict, dataclass
import numpy as np
import string

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

def leftMatmul(M, v):
    ret = np.array([0, 0, 0], int)
    for i, row in enumerate(M):
        for j, elem in enumerate(row):
            if elem > 0:
                ret[j] = toVector(v)[i]
            elif elem < 0:
                ret[j] = not toVector(v)[i]
    return toBinary(ret)

def rightMatmul(M, v):
    ret = np.array([0, 0, 0], int)
    for i, row in enumerate(M):
        for j, elem in enumerate(row):
            if elem > 0:
                ret[i] = toVector(v)[j]
            elif elem < 0:
                ret[i] = not toVector(v)[j]
    return toBinary(ret)

# Base pattern for most curves here
Ca00 = [0b000, 0b001, 0b011, 0b010, 0b110, 0b111, 0b101, 0b100]

@dataclass
class HilbertCurve:
    def __init__(self, name, X_1, X_2, Y = None, handedness = None, reverse = None, X_2_reverse = None):
        self.name = name
        self.Y = Y if Y else [i for i in range(8)] 
        self.X_1 = X_1
        self.X_2 = X_2
        self.handedness = handedness if handedness else [False for _ in range(8)]
        self.reverse = reverse if reverse else [False for _ in range(8)]
        self.X_2_reverse = X_2_reverse if X_2_reverse else X_2.copy()

    name: string
    Y: list[int]
    X_1: list[int]
    X_2: list[tuple]
    handedness: list[bool]
    reverse: list[bool]
    X_2_reverse: list[tuple]

Butz = HilbertCurve(
    name = 'butz',
    X_1 = Ca00,
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
)

Alfa = HilbertCurve(
    name = 'alfa',
    X_1 = Ca00,
    X_2 = Butz.X_2,
    handedness = [True, False, False, True, True, False, False, False],
    reverse = [False, False, True, False, True, False, True, True]
)

Harmonious = HilbertCurve(
    name = 'harmonious',
    X_1 = Ca00,
    X_2 = Butz.X_2,
    handedness = [True, True, False, True, True, False, True, True]
)

Basecamp = HilbertCurve(
    name = 'base_camp',
    X_1 = Ca00,
    X_2 = [
        (0b000, 0b001),
        (0b010, 0b110),
        (0b100, 0b000),
        (0b001, 0b101),
        (0b001, 0b101),
        (0b100, 0b000),
        (0b010, 0b110),
        (0b111, 0b110)
    ],
    handedness = [True, True, False, True, True, False, True, False],
    reverse= [False, True, False, True, False, True, False, True]
)

Sasburg = HilbertCurve(
    name = 'sasburg',
    X_1 = Ca00,
    X_2 = [
        (0b000, 0b001),
        (0b000, 0b010),
        (0b000, 0b100),
        (0b101, 0b100),
        (0b000, 0b001),
        (0b000, 0b100),
        (0b110, 0b100),
        (0b101, 0b100)
    ],
    handedness = [True, False, True, False, False, True, False, True]
)

Beta = HilbertCurve(
    name='beta',
    X_1 = Ca00,
    X_2 = [
        (0b101, 0b111),
        (0b110, 0b111),
        (0b101, 0b100),
        (0b101, 0b100),
        (0b000, 0b001),
        (0b000, 0b001),
        (0b011, 0b010),
        (0b011, 0b111),
    ],
    handedness = [False, True, True, False, False, True, True, True],
    reverse = [True, True, False, True, False, True, False, False]
)

Beta.X_2_reverse[0] = (0b011, 0b111)
Beta.X_2_reverse[7] = (0b011, 0b001)

# Beta musings
    #handedness_reverse = np.flip(handedness.copy())
    # TODO what's the correct one?
    # If the reversal is in fact a rotation instead of a mirroring[::-1]
    # X_2 reverse is just X_2
    # But what the hell is it, really?
    #handedness_reverse = np.array([False, False, False, True, True, False, False, False])
    #reverse_reverse = np.array([])

def stateTables(X_1, X_2, X_2_reverse, handedness, reverse, **kwargs):
    dY = list([i ^ j for i, j in X_2])
    TY = [np.stack((toVector(i), toVector(leftRotate(i, 1) if left else rightRotate(i, 1)), toVector(leftRotate(i, 2) if left else rightRotate(i, 2)))) for i, left in zip(dY, handedness)]

    for i in range(8):
        t = np.zeros((3, 3), int)
        for j in range(3):
            t[j, j] = -1 if X_2[i][0] & (4 >> j) else 1
        TY[i] = np.dot(TY[i], t)

    TY = list(zip(TY, reverse))

    dY_reverse = list([i ^ j for i, j in X_2_reverse])
    TY_reverse = [np.stack((toVector(i), toVector(leftRotate(i, 1) if left else rightRotate(i, 1)), toVector(leftRotate(i, 2) if left else rightRotate(i, 2)))) for i, left in zip(dY_reverse, handedness[::-1])]

    for i in range(8):
        t = np.zeros((3, 3), int)
        for j in range(3):
            t[j, j] = -1 if X_2_reverse[i][0] & (4 >> j) else 1
        TY_reverse[i] = np.dot(TY_reverse[i], t)

    TY_reverse = list(zip(TY_reverse, reverse[::-1]))

    reverse_state = 0
    reverse_states = {0: (np.identity(3, int), True)} # I think...
    for i, T in enumerate(TY_reverse):
        for j, mat in reverse_states.items():
            if (np.array_equal(T[0], mat[0]) and T[1] == mat[1]):
                break
        else:
            reverse_state = reverse_state + 1
            reverse_states[reverse_state] = T

    X1 = [[-1 for _ in range(8)]]
    for i, X_i in enumerate(X_1):
        X1[0][i] = X_i


    state = 0
    states = {0: (np.identity(3, int), False)}
    tm = [[-1 for _ in range(8)]]
    for i, T in enumerate(TY):
        for j, mat in states.items():
            if (np.array_equal(T[0], mat[0]) and T[1] == mat[1]):
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
        TMu, reverse_u = states[u]
        for i in range(8):
            j = rightMatmul(TMu, i)
            p = X1[0].index(j)
            X1[u][p] = i
            TMq, reverse_q = reverse_states[tm[0][p]] if reverse_u else states[tm[0][p]]
            TMw = np.dot(TMq, TMu)
            reverse_w = reverse_u ^ reverse_q
            for idx, mat in states.items():
                if (np.array_equal(TMw, mat[0]) and reverse_w == mat[1]):
                    tm[u][p] = idx
                    break
            else:
                state = state + 1
                states[state] = (TMw, reverse_w)
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

    return {
        'data3d':   X1, 
        'state3d':  tm, 
        'idata3d':  X1_inv, 
        'istate3d': tm_inv
    }

def tableToArray(name, data):
    contents = f'static unsigned const {name} [] = {{\n'
    for i in data:
        contents += '  '
        for j in i:
            contents += f'{j:>1}, '
        contents += '\n'
    contents = f'{contents[:-3]}\n}};\n'
    return contents

def main():
    for curve in (Butz, Alfa, Harmonious, Sasburg, Basecamp, Beta):
        print(curve.name)
        tables = stateTables(**asdict(curve))
        contents = ''
        for name, table in tables.items():
            contents += tableToArray(name=name, data=table)
            contents += '\n'
        with open(f'tables_{curve.name}.h', 'w') as f:
            print(contents, end='', file=f)

if __name__ == "__main__":
    main()