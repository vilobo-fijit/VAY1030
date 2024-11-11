#
# names: list[str] = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy",
#                     "Jack", "Katherine", "Liam", "Megan", "Nathan", "Olivia", "Georg", "Mike"]
# exam_results: dict[str, float] = {"Alice": 85.5, "Bob": 92.3, "Charlie": 68.9, "David": 88.4, "Eva": 91.2,
#                                   "Frank": 14, "Grace": 95.1, "Hannah": 43.8, "Ivy": 89.6, "Jack": 80.2,
#                                   "Katherine": 90, "Liam": 86.7, "Megan": 57.3, "Nathan": 93.5, "Olivia": 91.8,
#                                   "Vera": 92.7, "Walter": 76.5, "Xander": 85.3, "Yvonne": 77.9, "Zane": 89.0}
#
# column_width = 25
# 1.
# for name in names:
#     name_width = len(name)
#     result_width = 3
#     adjust_space = column_width - name_width - result_width
#     if name in exam_results:
#         result_with_adjust = str(exam_results[name]).rjust(adjust_space, " ")
#     else:
#         result_with_adjust = "--.-".rjust(adjust_space, " ")
#     print(f"{name.upper()}{result_with_adjust}")
#     print(f"{name.rjust(30,'v')}

if __name__ == '__main__':
    names: list[str] = [
        "Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy",
        "Jack", "Katherine", "Liam", "Megan", "Nathan", "Olivia", "Georg", "Mike"
    ]

    exam_results: dict[str, float] = {
        "Alice": 85.5, "Bob": 92.3, "Charlie": 68.9, "David": 88.4, "Eva": 91.2,
        "Frank": 14, "Grace": 95.1, "Hannah": 43.8, "Ivy": 89.6, "Jack": 80.2,
        "Katherine": 90, "Liam": 86.7, "Megan": 57.3, "Nathan": 93.5, "Olivia": 91.8,
        "Vera": 92.7, "Walter": 76.5, "Xander": 85.3, "Yvonne": 77.9, "Zane": 89.0
    }
    #for x in names:
    #    x = x.upper()
    #    print(f"{x}")



    for x in names:
        if exam_results.get(x) :
            if exam_results.get(x) < 50:
                staatus = "Failed"
            else:
                staatus = "Pass"

            score: str = f"{exam_results[x]:0.2f}"
            method_name(x, score, staatus)
        else:
            method_name(x, '--.--', "MISSED")