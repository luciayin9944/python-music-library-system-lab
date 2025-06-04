class Song:
    count = 0
    genres = []
    artists = []
    # genre_count = 0 #WRONG
    # artist_count = 0 #WRONG
    genre_count = {}
    artist_count = {}



    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)
        

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1

        
s1 = Song("99 Problems", "Jay Z", "Rap")
s2 = Song("Halo", "Beyonce", "Pop")
s3 = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

#accessing class attributes
print(Song.count)  #3
print(Song.genres)  #['Rap', 'Pop', 'Rock']
print(Song.artists)  #['Jay Z', 'Beyonce', 'Nirvana']
print(Song.genre_count)  #{'Rap': 1, 'Pop': 1, 'Rock': 1}
print(Song.artist_count)  #{'Jay Z': 1, 'Beyonce': 1, 'Nirvana': 1}

    

    



    
