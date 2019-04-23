import random
import time
import string
import random

from db import Database
from user import UserRepo
from album import AlbumRepo
from song import SongRepo
from tag import TagRepo

from faker import Faker
fake = Faker()

database = Database()
database.connect()

user_repo = UserRepo(database.conn)
album_repo = AlbumRepo(database.conn)
song_repo = SongRepo(database.conn)
tag_repo = TagRepo(database.conn)

# create many faker users
users = []
for x in range(0, 300):
    user = user_repo.create_user(
        email=fake.email(),
        display_name=fake.name(),
        password='password'
    )

    users.append(user)

# create some albums
albums = []
for x in range(0, 300):
    user = random.choice(users)

    album = album_repo.create_album(
        user_id=user.UserID,
        album_title=fake.sentence(nb_words=3),
        album_length=9
    )

    albums.append(album)

for album in albums:
    for x in range(1, random.randint(5, 12)):
        song = song_repo.insert_song(
            title=fake.sentence(nb_words=4),
            userid=album.UserID,
            albumid=album.AlbumID,
            length=random.randint(120,240),
            price=9.99
        )

#creating tags for testing
for x in range(0,100):
    tagName = fake.sentence(nb_words=3)
    
    tag_repo.create_tag(
        name=tagName
    )