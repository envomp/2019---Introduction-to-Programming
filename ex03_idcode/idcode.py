is_valid_gender_number, is_valid_year_number, is_valid_month_number, is_valid_day_number, is_leap_year, is_valid_birth_number, algorithm, algorithm2, is_valid_control_number, get_gender, get_full_year, get_birth_place, get_data_from_id, is_id_valid = lambda gender_number: gender_number in range(1, 7), lambda year_number: year_number in range(0, 100), lambda month_number: month_number in range(1, 13), lambda gender_number, year_number, month_number, day_number: (day_number in range(1, __import__("calendar").monthrange(get_full_year(gender_number, year_number), month_number)[1] + 1)), lambda year_number: (year_number % 4 == 0 and year_number % 100 != 0) or year_number % 400 == 0, lambda birth_number: birth_number in range(1, 1000), lambda id_code: sum(x * y for x, y in zip([int(x) for x in id_code], [1, 2, 3, 4, 5, 6, 7, 8, 9, 1])) % 11, lambda id_code: sum(x * y for x, y in zip([int(x) for x in id_code], [3, 4, 5, 6, 7, 8, 9, 1, 2, 3])) % 11, lambda id_code: algorithm(id_code) != 10 and algorithm(id_code) == int(id_code[10]) or algorithm(id_code) == 10 and algorithm2(id_code) != 10 and algorithm2(id_code) == int(id_code[10]) or algorithm2(id_code) == 10 and int(id_code[10]) == 0, lambda gender_number: "male" if gender_number % 2 != 0 else "female", lambda gender_number, year: (1800 + year if gender_number in range(0, 3) else 1900 + year if gender_number in range(3, 5) else 2000 + year), lambda birth_number: "Wrong input!" if 1 > birth_number or birth_number > 999 else {1 <= birth_number <= 10: "Kuressaare", 11 <= birth_number <= 20 or 271 <= birth_number <= 370: "Tartu", 21 <= birth_number <= 220 or 471 <= birth_number <= 490: "Tallinn", 221 <= birth_number <= 270: "Kohtla-Järve", 371 <= birth_number <= 420: "Narva", 421 <= birth_number <= 470: "Pärnu", 491 <= birth_number <= 520: "Paide", 521 <= birth_number <= 570: "Rakvere", 571 <= birth_number <= 600: "Valga", 601 <= birth_number <= 650: "Viljandi", 651 <= birth_number <= 710: "Võru", 711 <= birth_number <= 999: "undefined"}[True], lambda id_code: "Given invalid ID code!" if not is_id_valid(id_code) else f"This is a {get_gender(int(id_code[0]))} born on {id_code[5:7]}.{id_code[3:5]}.{get_full_year(int(id_code[0]), int(id_code[1:3]))} in {get_birth_place(int(id_code[7:10]))}.", lambda id_code: id_code.isnumeric() and len(id_code) == 11 and is_valid_gender_number(int(id_code[0])) and is_valid_year_number(int(id_code[1:3])) and is_valid_month_number(int(id_code[3:5])) and is_valid_day_number(int(id_code[0]), int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])) and is_valid_birth_number(int(id_code[7:10])) and is_valid_control_number(id_code)