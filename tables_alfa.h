static unsigned const data3d [] = {
0, 1, 3, 2, 6, 7, 5, 4, 
0, 4, 6, 2, 3, 7, 5, 1, 
0, 4, 5, 1, 3, 7, 6, 2, 
3, 1, 0, 2, 6, 4, 5, 7, 
6, 2, 3, 7, 5, 1, 0, 4, 
5, 7, 3, 1, 0, 2, 6, 4, 
5, 7, 6, 4, 0, 2, 3, 1, 
6, 4, 0, 2, 3, 1, 5, 7, 
0, 1, 5, 4, 6, 7, 3, 2, 
3, 2, 6, 7, 5, 4, 0, 1, 
0, 2, 3, 1, 5, 7, 6, 4, 
5, 4, 0, 1, 3, 2, 6, 7, 
6, 7, 5, 4, 0, 1, 3, 2, 
0, 2, 6, 4, 5, 7, 3, 1, 
3, 1, 5, 7, 6, 4, 0, 2, 
3, 7, 5, 1, 0, 4, 6, 2, 
3, 7, 6, 2, 0, 4, 5, 1, 
6, 2, 0, 4, 5, 1, 3, 7, 
6, 4, 5, 7, 3, 1, 0, 2, 
5, 4, 6, 7, 3, 2, 0, 1, 
5, 1, 0, 4, 6, 2, 3, 7, 
5, 1, 3, 7, 6, 2, 0, 4, 
3, 2, 0, 1, 5, 4, 6, 7, 
6, 7, 3, 2, 0, 1, 5, 4
};

static unsigned const state3d [] = {
1, 2, 2, 3, 3, 4, 4, 5, 
0, 8, 8, 7, 7, 9, 9, 6, 
10, 13, 13, 11, 11, 14, 14, 12, 
16, 15, 15, 0, 0, 17, 17, 11, 
18, 7, 7, 9, 9, 5, 5, 0, 
11, 19, 19, 15, 15, 0, 0, 4, 
20, 21, 21, 12, 12, 1, 1, 9, 
23, 12, 12, 1, 1, 22, 22, 20, 
13, 10, 10, 20, 20, 18, 18, 15, 
14, 3, 3, 4, 4, 6, 6, 1, 
2, 1, 1, 22, 22, 21, 21, 23, 
5, 6, 6, 2, 2, 3, 3, 17, 
17, 4, 4, 6, 6, 2, 2, 14, 
8, 0, 0, 17, 17, 19, 19, 16, 
9, 22, 22, 21, 21, 12, 12, 2, 
22, 9, 9, 5, 5, 8, 8, 18, 
3, 14, 14, 23, 23, 13, 13, 19, 
12, 23, 23, 13, 13, 11, 11, 3, 
4, 17, 17, 19, 19, 15, 15, 8, 
21, 20, 20, 18, 18, 16, 16, 13, 
6, 5, 5, 8, 8, 7, 7, 22, 
19, 11, 11, 14, 14, 23, 23, 10, 
15, 16, 16, 10, 10, 20, 20, 7, 
7, 18, 18, 16, 16, 10, 10, 21
};

static unsigned const idata3d [] = {
0, 1, 3, 2, 7, 6, 4, 5, 
0, 7, 3, 4, 1, 6, 2, 5, 
0, 3, 7, 4, 1, 2, 6, 5, 
2, 1, 3, 0, 5, 6, 4, 7, 
6, 5, 1, 2, 7, 4, 0, 3, 
4, 3, 5, 2, 7, 0, 6, 1, 
4, 7, 5, 6, 3, 0, 2, 1, 
2, 5, 3, 4, 1, 6, 0, 7, 
0, 1, 7, 6, 3, 2, 4, 5, 
6, 7, 1, 0, 5, 4, 2, 3, 
0, 3, 1, 2, 7, 4, 6, 5, 
2, 3, 5, 4, 1, 0, 6, 7, 
4, 5, 7, 6, 3, 2, 0, 1, 
0, 7, 1, 6, 3, 4, 2, 5, 
6, 1, 7, 0, 5, 2, 4, 3, 
4, 3, 7, 0, 5, 2, 6, 1, 
4, 7, 3, 0, 5, 6, 2, 1, 
2, 5, 1, 6, 3, 4, 0, 7, 
6, 5, 7, 4, 1, 2, 0, 3, 
6, 7, 5, 4, 1, 0, 2, 3, 
2, 1, 5, 6, 3, 0, 4, 7, 
6, 1, 5, 2, 7, 0, 4, 3, 
2, 3, 1, 0, 5, 4, 6, 7, 
4, 5, 3, 2, 7, 6, 0, 1
};

static unsigned const istate3d [] = {
1, 2, 3, 2, 5, 4, 3, 4, 
0, 6, 7, 7, 8, 9, 8, 9, 
10, 11, 12, 11, 13, 13, 14, 14, 
15, 15, 0, 16, 17, 17, 0, 11, 
5, 5, 7, 7, 0, 9, 18, 9, 
15, 15, 0, 19, 4, 11, 0, 19, 
12, 9, 1, 1, 12, 20, 21, 21, 
12, 22, 1, 1, 12, 22, 23, 20, 
13, 10, 15, 18, 20, 10, 20, 18, 
6, 1, 3, 14, 6, 4, 3, 4, 
2, 22, 1, 1, 23, 22, 21, 21, 
6, 2, 3, 2, 6, 5, 3, 17, 
6, 2, 14, 2, 6, 4, 17, 4, 
8, 16, 0, 19, 17, 17, 0, 19, 
12, 22, 2, 9, 12, 22, 21, 21, 
5, 5, 18, 22, 8, 9, 8, 9, 
23, 19, 23, 3, 13, 13, 14, 14, 
23, 11, 23, 11, 13, 13, 12, 3, 
15, 15, 8, 19, 17, 17, 4, 19, 
16, 13, 16, 18, 20, 21, 20, 18, 
5, 5, 7, 7, 8, 6, 8, 22, 
23, 11, 23, 11, 10, 19, 14, 14, 
16, 10, 16, 15, 20, 10, 20, 7, 
16, 10, 16, 18, 21, 10, 7, 18
};

