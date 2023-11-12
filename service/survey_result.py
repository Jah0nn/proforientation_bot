from repository.lang import translate


def calculatePercent(a, b, c):
    sp = (int(a) / 101) * 100
    dp = (int(b) / 97) * 100
    mp = (int(c) / 95) * 100
    res = [int(sp), int(dp), int(mp)]
    print(res)
    return res


def show_percent(sp, dp, mp):
    res = ''
    lst = [sp, dp, mp]
    print(lst)
    lst1 = sorted(lst, reverse=True)
    if lst1[0] == sp:
        sp += 30
        lst1[0] = lst1[0] + 30
    elif lst1[0] == dp:
        dp += 30
        lst1[0] = lst1[0] + 30
    elif lst1[0] == mp:
        mp += 30
        lst1[0] = lst1[0] + 30
    print(lst1)
    for i in lst1:
        if i == sp:
            res += f'{translate("comp_soft","ru")}:{sp}\n'
        elif i == dp:
            res += f'{translate("comp_design","ru")}:{dp}\n'
        else:
            res += f'{translate("comp_mark","ru")}:{mp}\n'
    return res

