reverse_accept_list = ['ZZ', 'YZ', 'YY', 'XZ', 'XY', 'XX', 'UZ', 'UY', 'UX', 'UU', 'SZ', 'SY', 'SX', 'SU', 'SS', 'RZ', 'RY', 'RX', 'RU', 'RS', 'RR', 'QZ', 'QY', 'QX', 'QU', 'QS', 'QR', 'QQ', 'PZ', 'PY', 'PX', 'PU', 'PS', 'PR', 'PQ', 'PP', 'OZ', 'OY', 'OX', 'OU', 'OS', 'OR', 'OQ', 'OP', 'OO', 'NZ', 'NY', 'NX', 'NU', 'NS', 'NR', 'NQ', 'NP', 'NO', 'NN', 'LZ', 'LY', 'LX', 'LU', 'LS', 'LR', 'LQ', 'LP', 'LO', 'LN', 'LL', 'KZ', 'KY', 'KX', 'KU', 'KS', 'KR', 'KQ', 'KP', 'KO', 'KN', 'KL', 'KK', 'JZ', 'JY', 'JX', 'JU', 'JS', 'JR', 'JQ', 'JP', 'JO', 'JN', 'JL', 'JK', 'JJ', 'IZ', 'IY', 'IX', 'IU', 'IS', 'IR', 'IQ', 'IP', 'IO', 'IN', 'IL', 'IK', 'IJ', 'II', 'HZ', 'HY', 'HX', 'HU', 'HS', 'HR', 'HQ', 'HP', 'HO', 'HN', 'HL', 'HK', 'HJ', 'HI', 'HH', 'GZ', 'GY', 'GX', 'GU', 'GS', 'GR', 'GQ', 'GP', 'GO', 'GN', 'GL', 'GK', 'GJ', 'GI', 'GH', 'GG', 'FZ', 'FY', 'FX', 'FU', 'FS', 'FR', 'FQ', 'FP', 'FO', 'FN', 'FL', 'FK', 'FJ', 'FI', 'FH', 'FG', 'FF', 'DZ', 'DY', 'DX', 'DU', 'DS', 'DR', 'DQ', 'DP', 'DO', 'DN', 'DL', 'DK', 'DJ', 'DI', 'DH', 'DG', 'DF', 'DD', 'CZ', 'CY', 'CX', 'CU', 'CS', 'CR', 'CQ', 'CP', 'CO', 'CN', 'CL', 'CK', 'CJ', 'CI', 'CH', 'CG', 'CF', 'CD', 'CC', 'BZ', 'BY', 'BX', 'BU', 'BS', 'BR', 'BQ', 'BP', 'BO', 'BN', 'BL', 'BK', 'BJ', 'BI', 'BH', 'BG', 'BF', 'BD', 'BC', 'BB']

eind_lijst = []
gekoppelde_letters = []
for p in reverse_accept_list:

    if p[0] not in gekoppelde_letters and p[1] not in gekoppelde_letters:

        gekoppelde_letters.append(p[0])
        gekoppelde_letters.append(p[1])
        eind_lijst.append(p)

print(gekoppelde_letters)


print(eind_lijst)
