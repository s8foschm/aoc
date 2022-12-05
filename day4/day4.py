def inc(lower_A, upper_A, lower_B, upper_B):
    return ((lower_B >= lower_A) and (lower_B <= upper_A)
            and (upper_B >= lower_A) and (upper_B <= upper_A))


def a_overlap_b(lower_A, upper_A, lower_B, upper_B):
    return ((lower_B >= lower_A) and (upper_B >= upper_A)
            and (lower_B <= upper_A))


with open('input.txt', 'r') as file:
    part_one_count = 0
    part_two_count = 0

    for line in file:

        line = line[:-1]
        (A, B) = line.split(",")
        (lower_A, upper_A) = A.split("-")
        (lower_B, upper_B) = B.split("-")
        (lower_A, upper_A, lower_B, upper_B) = \
            (int(lower_A), int(upper_A), int(lower_B), int(upper_B))

        if (lower_A > upper_A) or (lower_B > upper_B):
            raise ValueError(line, lower_A, upper_A, lower_B, upper_B)

        # ========== PART ONE ==========

        if inc(lower_A, upper_A, lower_B, upper_B) or inc(lower_B, upper_B, lower_A, upper_A):
            part_one_count += 1

        # ========== PART TWO ==========
        if inc(lower_A, upper_A, lower_B, upper_B) \
                or inc(lower_B, upper_B, lower_A, upper_A) \
                or a_overlap_b(lower_A, upper_A, lower_B, upper_B) \
                or a_overlap_b(lower_B, upper_B, lower_A, upper_A):
            part_two_count += 1

    print(part_one_count)
    print(part_two_count)
