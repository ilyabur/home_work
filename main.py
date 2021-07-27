# 8.6
def city_country():
    city = input("Please say your favourite city?: ")
    country = input("Please say your favourite country?: ")
    msg = city.title() + " and " + country.title()
    print(msg)
    return msg

# 8.7
def name_album(name, album, num_song=""):
    albom_name = {"first": name, "second": album}
    if num_song:
        albom_name["num_son"] = num_song
    return albom_name

# 8.8
def name_album_2(singer="", album=""):
    person = {"first": singer, "second": album}
    while True:
            print("For exit print 'quit' ")
            print("Please set your favourite singer and his album:")
            singer_x = input("Singer:")
            if singer_x == "quit":
                break
            album_x = input("Album:")
            if album_x == "quit":
                break
            sing = name_album_2(singer_x, album_x)
            return sing
            print(person)


name_album_2()

