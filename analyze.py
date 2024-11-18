import numpy as np
from sys import stderr, argv

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd, file=stderr)
    # Print New Line on Complete
    if iteration == total: 
        print(file=stderr)

coords = np.genfromtxt(argv[1])
x = coords[:,0]
xyz = coords[:, 1:4]
x_inv = coords[:, -1]
print(np.linalg.norm(x - x_inv, np.inf))

WL = [0, 0, 0]

printProgressBar(0, np.size(x) - 1)
for i in range(np.size(x) - 1):
    WLinf = np.max(np.power(np.linalg.norm(xyz[i+1:] - xyz[i], np.inf, axis=1), 3) / (x[i+1:] - x[i]))
    WL1 = np.max(np.power(np.linalg.norm(xyz[i+1:] - xyz[i], 1, axis=1), 3) / (x[i+1:] - x[i]))
    WL2 = np.max(np.power(np.linalg.norm(xyz[i+1:] - xyz[i], 2, axis=1), 3) / (x[i+1:] - x[i]))
    if (WLinf > WL[0]):
        WL[0] = WLinf
    if (WL1 > WL[1]):
        WL[1] = WL1
    if (WL2 > WL[2]):
        WL[2] = WL2
    printProgressBar(i+1, np.size(x) - 1)

WL = np.power(WL, 1./3)
print('WD1\tWD2\tWDinf')
print(f'{WL[1]}\t{WL[2]}\t{WL[0]}')

