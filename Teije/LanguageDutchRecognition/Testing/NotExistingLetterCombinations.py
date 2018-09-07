def FileReader(filename):
    try:
        with open(filename, "r") as reader:
            inputsent = reader.read()
    except:
        inputsent = filename.lower()

    return(inputsent)


def NonExist(filename):
    filename = FileReader(filename).lower()

    combolist = []
    wordlist = []
    notlist = []
    not2list = []

    for i in "abcdefghijklmnopqrstuvwxyz":
        for j in "abcdefghijklmnopqrstuvwxyz":
            combolist.append(i+j)

    for i in filename:
        if i.isalpha():
            wordlist.append(i.lower())
    word = "".join(wordlist)

    for i in combolist:
        if i not in word:
            notlist.append(i)

    for i in combolist:
        if i not in filename:
            not2list.append(i)

    print(notlist)
    print(not2list)

def CheckNoCombo(input):

    nolist = ['ah', 'ai', 'aj', 'ao', 'aq', 'au', 'av', 'aw', 'ax', 'az', 'bc', 'bd', 'bf', 'bg', 'bh', 'bj', 'bk', 'bm', 'bn', 'bp', 'bq', 'bs', 'bt', 'bv', 'bw', 'bx', 'by', 'bz', 'cb', 'cc', 'cd', 'cf', 'cg', 'cj', 'ck', 'cl', 'cm', 'cn', 'cp', 'cq', 'cs', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'dc', 'df', 'dg', 'dj', 'dl', 'dp', 'dq', 'dw', 'dx', 'dy', 'ej', 'eq', 'ex', 'ey', 'fc', 'fj', 'fk', 'fl', 'fn', 'fp', 'fq', 'fr', 'fs', 'fu', 'fx', 'fy', 'fz', 'gc', 'gf', 'gh', 'gj', 'gl', 'gp', 'gq', 'gx', 'gy', 'hb', 'hc', 'hd', 'hf', 'hg', 'hh', 'hj', 'hk', 'hl', 'hn', 'hp', 'hq', 'hs', 'hv', 'hw', 'hx', 'hy', 'hz', 'ih', 'ii', 'io', 'iq', 'iw', 'ix', 'iy', 'iz', 'jb', 'jc', 'jh', 'ji', 'jj', 'jl', 'jo', 'jp', 'jq', 'jr', 'js', 'jt', 'jw', 'jx', 'jy', 'kc', 'kf', 'kg', 'kp', 'kq', 'kx', 'ky', 'lc', 'lj', 'lq', 'lr', 'lx', 'ly', 'mc', 'mf', 'mg', 'mj', 'mk', 'ml', 'mn', 'mp', 'mq', 'mr', 'mx', 'my', 'nf', 'nj', 'nq', 'nx', 'ny', 'oa', 'oi', 'oj', 'oq', 'ox', 'oy', 'pb', 'pc', 'pf', 'pg', 'ph', 'pj', 'pk', 'pm', 'pn', 'pq', 'ps', 'pt', 'pw', 'px', 'py', 'qa', 'qb', 'qc', 'qd', 'qe', 'qf', 'qg', 'qh', 'qi', 'qj', 'qk', 'ql', 'qm', 'qn', 'qo', 'qp', 'qq', 'qr', 'qs', 'qt', 'qu', 'qv', 'qw', 'qx', 'qy', 'qz', 'rc', 'rf', 'rq', 'rr', 'rx', 'ry', 'sf', 'sj', 'sm', 'sq', 'su', 'sx', 'tc', 'tf', 'tq', 'tx', 'uc', 'uf', 'uh', 'uj', 'uo', 'up', 'uq', 'uv', 'ux', 'uy', 'uz', 'vb', 'vc', 'vd', 'vf', 'vg', 'vh', 'vj', 'vk', 'vm', 'vn', 'vp', 'vq', 'vs', 'vt', 'vv', 'vw', 'vx', 'vy', 'vz', 'wb', 'wc', 'wd', 'wf', 'wg', 'wh', 'wj', 'wk', 'wl', 'wm', 'wn', 'wp', 'wq', 'wr', 'ws', 'wt', 'wu', 'wv', 'ww', 'wx', 'wy', 'wz', 'xa', 'xb', 'xc', 'xd', 'xe', 'xf', 'xg', 'xh', 'xi', 'xj', 'xk', 'xl', 'xm', 'xn', 'xo', 'xp', 'xq', 'xr', 'xs', 'xt', 'xu', 'xv', 'xw', 'xx', 'xy', 'xz', 'ya', 'yb', 'yc', 'yd', 'ye', 'yg', 'yh', 'yj', 'yk', 'yl', 'ym', 'yn', 'yo', 'yp', 'yq', 'yr', 'yt', 'yv', 'yw', 'yx', 'yy', 'yz', 'zb', 'zc', 'zd', 'zf', 'zg', 'zh', 'zj', 'zk', 'zl', 'zm', 'zn', 'zp', 'zq', 'zr', 'zs', 'zt', 'zv', 'zx', 'zy', 'zz']

    inputlist = []
    for i in input:
        if i.isalpha():
            inputlist.append(i.lower())
    input = "".join(inputlist)

    counter = 0

    for i in nolist:
        if i in input:
            counter += input.count(i)
            print(i)

    ratio = counter / len(input)
    return(ratio)

if __name__ == "__main__":
    print(CheckNoCombo("alfabet"))
