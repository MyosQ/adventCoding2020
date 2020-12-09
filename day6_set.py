def read_file(file_name: str) -> list:
    return [list(map(set, line.splitlines())) for line in open(file_name, 'r').read().split('\n\n')]


def calc_num_questions(answers_set: list, part: str) -> int:

    num_ans = 0
    for group in answers_set:
        print(group)
        if part == 'part1':
            num_ans += len(set.union(*group))
        elif part == 'part2':
            num_ans += len(set.intersection(*group))
    return num_ans


if __name__ == '__main__':
    file_name = 'input6_test.txt'
    list_set_answers = read_file(file_name)
    print(list_set_answers)
    print(type(list_set_answers))
    print(type(list_set_answers[1][0]))
    questions_answered_part_1 = calc_num_questions(list_set_answers, 'part1')
    questions_answered_part_2 = calc_num_questions(list_set_answers, 'part2')
    print(questions_answered_part_1, questions_answered_part_2)
