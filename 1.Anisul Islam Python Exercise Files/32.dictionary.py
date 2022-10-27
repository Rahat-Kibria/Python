studentId = {
    "101": "Rahat Kibria",
    "102": "Hasan Kibria",
    "103": "Golam Kibria",
    "104": "Salma Kibria",
    105: "Hasina Fatema"
}
print(studentId["101"])
print(studentId.get("102"))
print(studentId.get("105", "Not a valid key"))
print(studentId.get(105, "Not a valid key"))