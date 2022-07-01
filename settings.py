from numpy import unique

DATAFRAME_SINAIS = {
    '0':[941,1339],
    '1':[697,1206],
    '2':[697,1339],
    '3':[697,1477],
    '4':[770,1206],
    '5':[770,1339],
    '6':[770,1477],
    '7':[852,1206],
    '8':[852,1339],
    '9':[852,1477],
    'A':[697,1633],
    'B':[770,1633],
    'C':[852,1633],
    'D':[941,1633],
    'X':[941,1206],
    '#':[941,1477]
}

F1_VALUES = unique([value[0] for value in DATAFRAME_SINAIS.values()])
F2_VALUES = unique([value[1] for value in DATAFRAME_SINAIS.values()])

DURATION = 2
AMPLITUDE = 2
FS = 44100

COLORS = ['green','orange','red']