users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
countUsers = len(users)
uniqueVisits = len(set(users))
usersDict = {
    "Общее количество":0,
    "Уникальные посещения":0
}
usersDict["Общее количество"] = countUsers
usersDict["Уникальные посещения"] = uniqueVisits

print(usersDict)