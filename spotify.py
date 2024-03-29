import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageFont
import textwrap
from dotenv import load_dotenv
import os
typeface = 'assets/fonts/FreeSansBold.otf'

load_dotenv()

def Spotify(Show, draw):
    fSong = ImageFont.truetype(
        typeface, 21)
    fArtist = ImageFont.truetype(
        typeface, 18)

    bmp = Image.open("assets/spotify-invert.bmp")
    Show.paste(bmp, (4, 92))
    draw.rectangle((1, 90, 87, 178), width=3)

    try:
        scope = "user-read-currently-playing"

        client_id = os.getenv("SPOTIPY_CLIENT_ID")
        client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
        redirect = os.getenv("SPOTIPY_REDIRECT_URI")

        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=client_id, client_secret=client_secret, redirect_uri=redirect, scope=scope))

        results = sp.current_user_playing_track()

        if results == None:
            draw.text((90, 92), "Nothing is \nPlaying", font=fSong, fill=None)
        else:
            song = (results["item"]["name"])
            artist = (results["item"]["artists"][0]["name"])

            if len(song) > 16:
                songwrap = textwrap.TextWrapper(width=16)
                song_list = songwrap.wrap(text=song)
                wrapsong = song_list[0] + "\n" + song_list[1]
                draw.text((90, 92), wrapsong, font=fSong, fill=None)
                if len(artist) > 19:
                    artistwrap = textwrap.TextWrapper(width=19)
                    artist_list = artistwrap.wrap(text=artist)
                    wrapartist = artist_list[0] + "\n" + artist_list[1]
                    draw.text((90, 137), wrapartist, font=fArtist, fill=None)
                else:
                    draw.text((90, 137), artist, font=fArtist, fill=None)
            else:
                draw.text((90, 92), song, font=fSong, fill=None)
                if len(artist) > 19:
                    artistwrap = textwrap.TextWrapper(width=19)
                    artist_list = artistwrap.wrap(text=artist)
                    wrapartist = artist_list[0] + "\n" + artist_list[1]
                    draw.text((90, 118), wrapartist, font=fArtist, fill=None)
                else:
                    draw.text((90, 118), artist, font=fArtist, fill=None)
        return
    except:
        from datetime import datetime
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("An error occured, It will try again at the start of the next minute")
        print(current_time)
        draw.text((90, 94), "An error \noccurred", font=fSong, fill=None)
        return