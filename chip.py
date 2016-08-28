from pytube import YouTube
from moviepy.editor import *

f = open('shit.txt','r').read().split('\n')[:-1]
pieces = [x.split(' ') for x in f]

fmat = 'mp4'

filename_list = []
slice_list = []


for i in pieces:
  url = i[0]
  rest = i[1:]

  slices = [rest[i:i+2] for i in range(0,len(rest),2)]
  slice_list.append(slices)
  yt = YouTube(url)
  yt.filter(fmat)[-1]
  b = yt.filename+'.'+fmat
  filename_list.append(str(b))
  video = yt.get(fmat)
  video.download('/Users/flott/')



clipstack = []
z = zip(filename_list,slice_list)


for i in z:
    for j in range(0,len(i[1])):
        #print i[0],int(i[1][j][0]),int(i[1][j][1])
        clip = VideoFileClip(i[0]).subclip(int(i[1][j][0]),int(i[1][j][1]))
        clipstack.append(clip)


#clip = VideoFileClip(filename_list[i]).subclip(slice_list[i][j][0],slice_list[i][j][1])
#clipstack.append(clip)


#print clipstack[1]





#clip1 = VideoFileClip(z[0][0]).subclip(4,44)
#print clip1



final_clip = concatenate_videoclips(clipstack,method="compose")
final_clip.write_videofile("movie.mp4")


