users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
count_Users = len(users)
unique_Visits = len(set(users))

users_Dict = {"Общее количество": count_Users, "Уникальные посещения": unique_Visits}

print(users_Dict)
