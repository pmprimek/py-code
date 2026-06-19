marks = {
    "prince": 100,
    "satyam": 56,
    "akash": 23,
}
print(marks.items())  # Key-value pairs dikhata hai
print(marks.keys())   # Sabhi keys dikhata hai
print(marks.values())  # Sabhi values dikhata hai
marks.update({"prince": 99,"sameer": 95})
print(marks)
print(marks.get("prince2"))    # print non
print(marks["prince2"])     # return as error


