def parse_input():
    with open("resources/day14.txt") as file:
        polymer_template = file.readline().rstrip()
        file.readline()

        insertion_rules = {}
        while rule := file.readline().rstrip():
            rule_split = rule.split(" -> ")
            insertion_rules[rule_split[0]] = rule_split[1]

    return polymer_template, insertion_rules


def polymer_insertion(polymer_template, insertion_rules):
    i = 1
    while i < len(polymer_template):
        pair = polymer_template[i - 1] + polymer_template[i]
        polymer_template = polymer_template[:i] + insertion_rules[pair] + polymer_template[i:]
        i += 2

    return polymer_template


def run_polymer_insertions(polymer_template, insertion_rules, step):
    for i in range(0, step):
        polymer_template = polymer_insertion(polymer_template, insertion_rules)

    return polymer_template


def solution1():
    polymer_template, insertion_rules = parse_input()

    polymer_template = run_polymer_insertions(polymer_template, insertion_rules, 10)

    char_freq = {}
    for i in polymer_template:
        char_freq[i] = char_freq[i] + 1 if i in char_freq else 1

    return max(char_freq.values()) - min(char_freq.values())


class PolymerTemplate(object):
    def __init__(self, poly_map, first_pair, last_pair):
        self.poly_map = poly_map
        self.first_pair = first_pair
        self.last_pair = last_pair

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"PolymerTemplate({self.poly_map}, {self.first_pair}, {self.last_pair})"


def polymer_insertion_optimized(polymer_template, insertion_rules):
    new_poly_map = {}
    poly_map = polymer_template.poly_map
    for i in poly_map:
        first_pair = i[0] + insertion_rules[i]
        second_pair = insertion_rules[i] + i[1]

        new_poly_map[first_pair] = poly_map[i] if first_pair not in new_poly_map else poly_map[i] + new_poly_map[
            first_pair]
        new_poly_map[second_pair] = poly_map[i] if second_pair not in new_poly_map else poly_map[i] + new_poly_map[
            second_pair]

    first_pair = polymer_template.first_pair[0] + insertion_rules[polymer_template.first_pair]
    last_pair = insertion_rules[polymer_template.last_pair] + polymer_template.last_pair[1]

    return PolymerTemplate(new_poly_map, first_pair, last_pair)


def run_polymer_insertions_optimized(polymer_template, insertion_rules, step):
    for i in range(0, step):
        polymer_template = polymer_insertion_optimized(polymer_template, insertion_rules)

    return polymer_template


def solution2():
    poly_template_str, insertion_rules = parse_input()

    polymer_template_map = {}
    for i in range(0, len(poly_template_str) - 1):
        pair = poly_template_str[i] + poly_template_str[i + 1]
        polymer_template_map[pair] = polymer_template_map[pair] + 1 if pair in polymer_template_map else 1

    polymer_template = PolymerTemplate(polymer_template_map, poly_template_str[:2], poly_template_str[-2:])
    polymer_template = run_polymer_insertions_optimized(polymer_template, insertion_rules, 40)

    poly_map = polymer_template.poly_map
    char_freq = {}
    for i in poly_map.keys():
        for j in list(i):
            char_freq[j] = char_freq[j] + poly_map[i] if j in char_freq else poly_map[i]

    char_freq[polymer_template.first_pair[0]] += 1
    char_freq[polymer_template.last_pair[1]] += 1

    return (max(char_freq.values()) - min(char_freq.values())) / 2


print(solution1())
print(solution2())
