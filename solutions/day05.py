from enum import Enum


def parse_input():
    with open("resources/day05.txt") as file:
        vents = []
        while points := file.readline():
            vents.append([tuple(map(int, x.split(","))) for x in points.rstrip().split(" -> ")])

    return vents


class VentOrientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


def find_vents(vent_same_axis, vent_diff_axis, vent_orientation, vents_dict):
    if vent_same_axis[0] == vent_same_axis[1]:
        min_vent = min(vent_diff_axis[0], vent_diff_axis[1])
        max_vent = max(vent_diff_axis[0], vent_diff_axis[1])
        line_of_vents = []

        if vent_orientation == VentOrientation.HORIZONTAL:
            line_of_vents = [(i, vent_same_axis[0]) for i in (range(min_vent, max_vent + 1))]
        elif vent_orientation == VentOrientation.VERTICAL:
            line_of_vents = [(vent_same_axis[0], i) for i in (range(min_vent, max_vent + 1))]

        for i in line_of_vents:
            if i in vents_dict:
                vents_dict[i] = 1
            else:
                vents_dict[i] = 0

    return vents_dict


def solution1():
    vents, vents_dict = parse_input(), {}

    for vent_ends in vents:
        find_vents(
            (vent_ends[0][1], vent_ends[1][1]),
            (vent_ends[0][0], vent_ends[1][0]),
            VentOrientation.HORIZONTAL,
            vents_dict
        )
        find_vents(
            (vent_ends[0][0], vent_ends[1][0]),
            (vent_ends[0][1], vent_ends[1][1]),
            VentOrientation.VERTICAL,
            vents_dict
        )

    return sum(vents_dict.values())


def solution2():
    vents, vents_dict = parse_input(), {}

    for vent_ends in vents:
        find_vents(
            (vent_ends[0][1], vent_ends[1][1]),
            (vent_ends[0][0], vent_ends[1][0]),
            VentOrientation.HORIZONTAL,
            vents_dict
        )
        find_vents(
            (vent_ends[0][0], vent_ends[1][0]),
            (vent_ends[0][1], vent_ends[1][1]),
            VentOrientation.VERTICAL,
            vents_dict
        )

        # Diagonals
        if vent_ends[0][1] != vent_ends[1][1] and vent_ends[0][0] != vent_ends[1][0]:
            line_of_vents = [vent_ends[0]]

            iter_vent = list(vent_ends[0])
            while iter_vent != list(vent_ends[1]):
                if iter_vent[0] < vent_ends[1][0]:
                    iter_vent[0] = iter_vent[0] + 1
                else:
                    iter_vent[0] = iter_vent[0] - 1

                if iter_vent[1] < vent_ends[1][1]:
                    iter_vent[1] = iter_vent[1] + 1
                else:
                    iter_vent[1] = iter_vent[1] - 1

                line_of_vents.append(tuple(iter_vent))

            for vent in line_of_vents:
                if vent in vents_dict:
                    vents_dict[vent] = 1
                else:
                    vents_dict[vent] = 0

    return sum(vents_dict.values())


print(solution1())
print(solution2())
