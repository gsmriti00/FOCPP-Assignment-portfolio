staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

staff = staff.union({"Mark", "Ringo"})
staff_directors = staff.intersection(directors)
external = directors.difference(staff)
staff_or_external = directors.symmetric_difference(staff)

print(staff)
print(staff_directors)
print(external)
print(staff_or_external)
