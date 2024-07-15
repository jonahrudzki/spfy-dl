class Track:
    def __init__(self, track_name, album_name, album_img_url, artist_name):
        self.track_name = track_name
        self.album_name = album_name
        self.album_img_url = album_img_url
        self.artist_name = artist_name
        self.yt_url = None
    
    def get_track_name(self) -> str:
        return self.track_name
    
    def get_album_name(self) -> str:
        return self.album_name
    
    def get_album_img(self) -> str:
        return self.album_img_url
    
    def get_artist_name(self) -> str:
        return self.artist_name
    
    def get_url(self) -> str:
        return self.yt_url
    
    def set_url(self, url: str):
        self.yt_url = url