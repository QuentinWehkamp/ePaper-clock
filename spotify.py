import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageDraw, ImageFont

def Spotify(Show, draw):
    scope = "user-read-currently-playing"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.current_user_playing_track()

    song = (results["item"]["name"])
    artist = (results["item"]["artists"][0]["name"])
    
    fSong = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 20)
    fArtist = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeSansBold.ttf', 17)
    
    bmp = Image.open("spotify-invert.bmp")
    Show.paste(bmp,(4, 92))
    draw.rectangle((1, 90, 87, 178), width=3)
    draw.text((90, 94), song, font=fSong, fill=None)
    draw.text((90, 116), artist, font=fArtist, fill=None)