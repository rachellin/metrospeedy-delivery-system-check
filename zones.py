tabs = {
    "bklyn": {
        "northcentral brooklyn": [11222, 11237, 11206, 11205, 11221, 11216, 11213, 11233, 11203, 11212, 11207, 11208, 11211],
        "southern brooklyn": [11201, 11217, 11238, 11231, 11215, 11225, 11226, 11218, 11232, 11220, 11219, 11230, 11204, 11228, 11209, 11214, 11223, 11229, 11235, 11224, 11210]
    },
    "man": {
        "upper west side": [10023, 10024, 10025, 10125, 10132, 10133], 
        "upper manhattan": [10115, 10026, 10027, 10030, 10040, 10037, 10039, 10031, 10032, 10033, 10034], 
        "upper east side": [10021, 10028, 10065, 10075, 10128, 10131, 10162, 10029, 10130], 
        "midtown manhattan": [10001, 10010, 10016, 10017, 10022, 10019, 10020, 10036, 10101, 10102, 10103, 10105, 10106, 10107, 10108, 10109, 10110, 10111, 10112, 10113, 10114, 10116, 10117, 10118, 10119, 10120, 10121, 10122, 10123, 10124, 10126, 10129, 10138, 10150, 10151, 10152, 10153, 10154, 10155, 10156, 10157, 10158, 10159, 10160, 10163, 10164, 10165, 10166, 10167, 10168, 10169, 10170, 10171, 10172, 10173, 10174, 10175, 10176, 10177, 10178, 10179, 10185, 10199, 10104], 
        "downtown manhattan": [10002, 10003, 10009, 10004, 10005, 10006, 10011, 10012, 10013, 10014, 10282, 10280, 10048, 10007, 10038, 10279, 10271, 10270, 10045, 10018, 10242, 10249, 10256, 10258, 10259, 10260, 10261, 10268, 10269, 10272, 10274, 10275, 10276, 10277, 10278, 10281, 10285, 10286, 10008, 10015, 10041, 10043, 10055, 10060, 10069, 10080, 10081, 10087, 10090, 10095, 10161, 10203, 10211, 10212, 10213, 10273, 10265]
    },
    "wc": {
        "NW WC": [10547, 10598, 10562, 10510, 10588, 10566, 10511, 10548, 10520, 10546, 10527, 10501, 10505, 10589, 10535, 10596, 10567, 10540, 10517, 10587, 10514],
        "NE WC": [10560, 10597, 10507, 10506, 10576, 10549, 10504, 10590, 10518, 10570, 10519, 10526, 10536],
        "SE WC": [10604, 10603, 10595, 10577, 10573, 10605, 10528, 10543, 10538, 10804, 10801, 10803, 10601, 10606, 10594, 10805, 10580, 10578, 10553,10583],
        "SW WC": [10591, 10523, 10533, 10522, 10502, 10530, 10706, 10710, 10704, 10550, 10552, 10708, 10707, 10709, 10607, 10532, 10703, 10701, 10503, 10702]
    },
    "li": {
        "western LI": [11051,11052,11053,11023,11024,11026, 11575, 11020,11021,11042, 11030,11050,11576, 11501,11514, 11507,11577, 11596, 11040,11042, 11545,11548,11568]
    },
    "si": {
        "SI": [10302, 10303, 10310, 10306, 10307, 10308, 10309, 10312, 10301, 10304, 10305, 10314]
    },
    "bronx": {
        "bronx": [10461, 10462,10464, 10465, 10472, 10473, 10466, 10469, 10470, 10475, 10463, 10471, 10454, 10455, 10459, 10474, 10451, 10452, 10456, 10458, 10467, 10468, 10453, 10457, 10460]
    },
    "queens": {
        "jfk": [11430, 11691, 11697, 11695, 11694, 11693, 11692, 11096],
        "NW queens": [11101, 11102, 11103, 11377, 11104, 11373, 11372, 11368, 11378, 11374, 11375, 11379, 11385, 11418, 11415, 11105, 11106, 11109, 11369, 11120],
        "southern queens": [11421, 11417, 11414, 11420, 11433, 11412, 11411, 11413, 11422, 11434, 11416, 11419, 11429, 11436, 11435],
        "NE": [11356, 11357, 11361, 11363, 11004, 11426, 11364, 11428, 11423, 11432, 11427, 11354, 11358, 11359, 11360, 11362, 11365, 11366, 11005, 11355, 11367]
    },
    "ct": {
        "ct": ["06830", "06831", "06836", "06807", "06878", "06870"] 
    },
    "nj": {
        "nj": ["07024", "07030", "07086", "07030", "07032", "07087", "07094", "07097", "07302", "07303", "07304", "07305", "07306", "07307", "07308", "07310", "07311", "07395", "07399", "07086", "07020", "07093"]
    }
}

zip_check_data = []
fieldnames = ["zone", "equal", "diff1", "diff2"]

#total = 0
allzips = []
for region in tabs.values():
    for zone in region.values():
        allzips = allzips + zone
    
print(len(allzips))