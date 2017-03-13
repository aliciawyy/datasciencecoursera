"""
- https://community.topcoder.com/stat?c=problem_statement&pm=1918&rd=5006
get_flower_order
"""


def get_flower_order(height, bloom, wilt):
    flowers = zip(height, bloom, wilt)
    # Sort the flowers to make the height in ascending order
    flowers.sort()

    def is_overlap(f1, f2):
        # There is overlap when start1 <= end2 and start2 <= end1
        return f1[1] <= f2[2] and f2[1] <= f1[2]

    ordered = []
    for i, f in enumerate(flowers):
        pos = i
        # All the flowers are ordered before i
        while pos > 0 and not is_overlap(f, ordered[pos - 1]):
            pos -= 1
        ordered.insert(pos, f)
    result = [f[0] for f in ordered]
    return result



