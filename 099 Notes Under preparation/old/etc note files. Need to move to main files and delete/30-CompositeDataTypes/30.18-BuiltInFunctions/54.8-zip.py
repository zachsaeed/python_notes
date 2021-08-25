# Enumerate and zip are two of the most powerful tools when constructing a for-loop
# zip
# returns an iterator that aggregates elements from each of the iterables
# Returns an iterator of tuples where the i-th tuple contains the i-th
# element from each of the argument sequences or iterables
# Note: The iterator stops when the shortest input iterable is exhausted

# Two input lists
first_zip = zip([1, 2, 3], [4, 5, 6])
print(first_zip)  # <zip object at 0x0100CC60>  is an iterator of tuples
print(list(first_zip))  # [(1, 4), (2, 5), (3, 6)]  # list of tuples
# {}  empty because these iterators are exhausted and therefore empty
print(dict(first_zip))
# after iterating over them once. Will work fine after re-zipping
first_zip = zip([1, 2, 3], [4, 5, 6])
print(dict(first_zip))  # {1: 4, 2: 5, 3: 6}


# Three input lists throw an error when converted to dict
first_zip1 = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(list(first_zip1))  # (1, 4, 7), (2, 5, 8), (3, 6, 9)]  # list of tupes
first_zip2 = zip([1, 2, 3], [4, 5, 6], [7, 8, 9])
# print(dict(first_zip2))  # (ValueError: dictionary update sequence
# element #0 has length 3; 2 is required

# Note: we can unpack and existing list of tuples and zip them using *
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*five_by_two)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

# Example  match each student with the highest grades and generate a dictionary
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']
# returns dict with {student:highest score} USING DICT COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

# returns dict with {student:highest score} (same thing as above) USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)
print(final_grades)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: ((pair[0] + pair[1]) / 2),
            zip(midterms, finals)
        )
    )
)
print(avg_grades)
