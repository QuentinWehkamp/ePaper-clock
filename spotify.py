import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageDraw, ImageFont
import textwrap
from dotenv import load_dotenv
import os

load_dotenv()

def Spotify(Show, draw):
    fSong = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 20)
    fArtist = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 17)
    
    bmp = Image.open("assets/spotify-invert.bmp")
    Show.paste(bmp,(4, 92))
    draw.rectangle((1, 90, 87, 178), width=3)

    scope = "user-read-currently-playing"

    client_id = os.getenv("SPOTIPY_CLIENT_ID")
    client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
    redirect = os.getenv("SPOTIPY_REDIRECT_URI")

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect, scope=scope))

    results = sp.current_user_playing_track()
   
    if results == None:
        draw.text((90, 94), "Nothing is \nPlaying", font=fSong, fill=None)
    else:
        song = (results["item"]["name"])
        artist = (results["item"]["artists"][0]["name"])

        if len(song) > 16:
            songwrap = textwrap.TextWrapper(width=16)
            song_list = songwrap.wrap(text=song)
            wrapsong = song_list[0] + "\n" + song_list[1]
            draw.text((90, 94), wrapsong, font=fSong, fill=None)
            if len(artist) > 19:
                artistwrap = textwrap.TextWrapper(width=19)
                artist_list = artistwrap.wrap(text=artist)
                wrapartist = artist_list[0] + "\n" + artist_list[1]    
                draw.text((90, 135), wrapartist, font=fArtist, fill=None)
            else:
                draw.text((90, 135), artist, font=fArtist, fill=None)
        else:
            draw.text((90, 94), song, font=fSong, fill=None)
            if len(artist) > 19:
                artistwrap = textwrap.TextWrapper(width=19)
                artist_list = artistwrap.wrap(text=artist)
                wrapartist = artist_list[0] + "\n" + artist_list[1]
                draw.text((90, 116), wrapartist, font=fArtist, fill=None)
            else:
                draw.text((90, 116), artist, font=fArtist, fill=None)