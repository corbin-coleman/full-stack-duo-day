#!usr/bin/python3

def close_pairs(pairs=[]):
    if pairs is None:
        return False
    checked_pair = 0
    for point_1 in pairs:
        for point_2 in pairs:
            if point_1 is point_2:
                side_1 = point_2[0] - point_1[0]
                side_2 = point_2[1] - point_1[1]
                distance = (side_1 * side_1 + side_2 * side_2) ** 0.5
                if checked_pair == 0:
                    closest_dist = distance
                    closest_pair = [point_1, point_2]
                    checked_pair = 1
                elif distance < closest_dist:
                    closest_dist = distance
                    closest_pair = [point_1, point_2]
    return closest_pair
