def rozm_tab(d):
    i = 0
    while i * i < d:
        i += 1
    return i

sz = 'BTLLTU_ĘL_EOYPM_ĄPJZLCYNDREOKYLI_ZMFO_ĄGJY_Ó_N_DEWFWGISYSII_ŁEI_'
d = len(sz)
n = rozm_tab(d)
tab = [[''] * n] * n

i_sz = 0

for k in range(n):
    for w in range(n):
        tab[w][k] = sz[i_sz]
        i_sz += 1

print(tab)