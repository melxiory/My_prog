import itertools


def count_col_triang(input_):
    dict_points = {}
    for keys in input_:
        if keys[1] not in dict_points:
            dict_points[keys[1]] = [keys[0]]
        else:
            dict_points[keys[1]] += [keys[0]]
    numb_colors = len(dict_points.keys())
    numb_points = len(input_)
    for dict_keys in dict_points:
        comb_triang = list(itertools.combinations(dict_points[dict_keys], 3))
        if not comb_triang or len(comb_triang[0]) < 3:
            dict_points[dict_keys] = 0
            continue
        numb_triag = 0
        for points_triang in comb_triang:
            if points_triang[0][0]*(points_triang[1][1]-points_triang[2][1])+points_triang[1][0]*(points_triang[2][1]-points_triang[0][1])+points_triang[2][0]*(points_triang[0][1]-points_triang[1][1]):
                numb_triag += 1
        else:
            dict_points[dict_keys] = numb_triag
    total_numb_triang = sum(dict_points.values())
    max_triang = max(dict_points.values())
    name_points = [i for i in dict_points if dict_points[i] == max_triang]
    return [numb_points, numb_colors, total_numb_triang, sorted(name_points) + [max_triang] if max_triang else []]

print(count_col_triang([[[776, -828], 'cream'], [[-62, -269], 'silver'], [[-741, 375], 'violet'], [[-238, 171], 'violet'], [[-671, 914], 'lime'], [[-777, -454], 'violet'], [[142, 892], 'violet'], [[-21, 951], 'sky_blue'], [[205, 180], 'violet'], [[-339, -847], 'lime'], [[-903, 203], 'sky_blue'], [[-333, -82], 'cream'], [[-851, 330], 'cream'], [[-212, 314], 'sky_blue'], [[228, 796], 'lime'], [[-913, -897], 'violet'], [[458, 221], 'sky_blue'], [[-159, 501], 'lime'], [[-808, -86], 'cream'], [[395, -682], 'lime'], [[627, -781], 'lime'], [[216, -382], 'violet'], [[710, 886], 'cream'], [[-203, 623], 'violet'], [[314, -308], 'violet'], [[757, -824], 'sky_blue'], [[431, -281], 'silver'], [[-228, 146], 'red'], [[-316, 574], 'red'], [[671, 650], 'lime'], [[-9, -28], 'lime'], [[-242, -902], 'red'], [[520, 377], 'cream'], [[963, 860], 'sky_blue'], [[852, 750], 'violet'], [[125, -500], 'sky_blue'], [[352, 251], 'cream'], [[-669, -211], 'red'], [[984, 716], 'cream'], [[83, 522], 'cream'], [[560, -750], 'red'], [[-56, -55], 'cream'], [[168, 274], 'red'], [[-952, 650], 'cream'], [[-63, -287], 'lime'], [[-969, -210], 'violet'], [[384, -616], 'lime'], [[125, -875], 'violet'], [[817, -183], 'silver'], [[-631, -743], 'lime'], [[827, 684], 'cream']]))
