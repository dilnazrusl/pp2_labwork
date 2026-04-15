import pygame
import os


class MusicPlayer:
    def __init__(self, music_folder):
        pygame.mixer.init()
        self.music_folder = music_folder

        self.playlist = [
            os.path.join(music_folder, file)
            for file in os.listdir(music_folder)
            if file.endswith(".wav") or file.endswith(".mp3")
        ]

        self.current_track_index = 0
        self.is_playing = False

    def play(self):
        if not self.playlist:
            print("Playlist is empty!")
            return

        track = self.playlist[self.current_track_index]
        pygame.mixer.music.load(track)
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return

        self.current_track_index = (self.current_track_index + 1) % len(self.playlist)
        self.play()

    def previous_track(self):
        if not self.playlist:
            return

        self.current_track_index = (self.current_track_index - 1) % len(self.playlist)
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No track"
        return os.path.basename(self.playlist[self.current_track_index])

    def get_position(self):
        return pygame.mixer.music.get_pos() // 1000  # seconds
