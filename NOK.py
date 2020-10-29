def min_divider(count, dict_min_div):
    if count == 1:
        return dict_min_div
    else:
        a = 1
        while a < count**0.5:
            a += 1
            if count % a == 0:
                if a in dict_min_div:
                    dict_min_div[a] = dict_min_div[a] + 1
                else:
                    dict_min_div[a] = 1
                new_count = count / a
                return min_divider(new_count, dict_min_div)
        if count in dict_min_div:
            dict_min_div[int(count)] = dict_min_div[count] + 1
        else:
            dict_min_div[int(count)] = 1
        return min_divider(1, dict_min_div)

def nok(*a):
    s_itog = {}
    for i in a:
        i = min_divider(i, {})
        for key, value in i.items():
            if key in s_itog:
                if value <= s_itog[key]:
                    continue
                else:
                    s_itog[key] = s_itog[key] + (value - s_itog[key])
            else:
                s_itog[key] = value
    k = []
    for key, value in s_itog.items():
        k.append(key ** value)
    fin = 1
    for i in k:
       fin = fin * i
    return fin

print(nok(180, 50, 30, 100, 77135, 3416314, 347157, 23523, 43634724572457, 44))
