from moviepy.editor import *
import pygame

pygame.display.set_mode((0,0), 0, 32)
clip = VideoFileClip('audio/output.mp4').resize((1920,1080))
clip.preview()
pygame.quit()