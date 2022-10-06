from nested_data import albums

SONGS_LIST_INDEX = 3
ARTIST_LIST_INDEX = 1

while True:
    #-------------------------------------------------------------------------------#
    #Album menu print + input
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}, by {} ({})"
              .format(index + 1, title, artist, year))
    user_input_album = int(input())
    
    #Breaks if out of range
    if (user_input_album > len(albums)) or (user_input_album < 1):
        print("Finished - albums")
        break
    print()

    #-------------------------------------------------------------------------------#
    #Song menu print + input    
    print("Please choose your song (invalid choice exits):")
    for index_song, song in albums[user_input_album - 1][SONGS_LIST_INDEX]:
        print("{}: {}"
              .format(index_song, song))
    user_input_song = int(input())
    print()

    #Breaks if out of range
    if (user_input_song > len(albums[user_input_album - 1][SONGS_LIST_INDEX])) or (user_input_song < 1):
        continue

    #-------------------------------------------------------------------------------#
    #Song output with artist name
    print("Now playing: {}, by {}"
          .format(albums[user_input_album - 1][SONGS_LIST_INDEX][user_input_song-1][ARTIST_LIST_INDEX],
                  albums[user_input_album - 1][ARTIST_LIST_INDEX]))
    print()