



import cv2
#from colorthief import ColorThief
import numpy as np
import pandas as pd
import matplotlib.image as mpimg





import extcolors

from colormap import rgb2hex





camera=cv2.VideoCapture(0)
while True:
    _, image=camera.read()
    cv2.imshow('image', image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg', image)
        break
camera.release()
cv2.destroyAllWindows()
#def getcolor():
    #ColorThief=ColorThief('test1.jpg')
    #colors=ColorThief.get_pallete(color_count=2)
    #print(colors)
#getcolor()





colors_x = extcolors.extract_from_path('test1.jpg', tolerance = 12, limit = 12)
colors_x




def color_to_df(input):
    colors_pre_list = str(input).replace('([(','').split(', (')[0:-1]
    df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]
    df_percent = [i.split('), ')[1].replace(')','') for i in colors_pre_list]
    
    #convert RGB to HEX code
    df_color_up = [rgb2hex(int(i.split(", ")[0].replace("(","")),
                          int(i.split(", ")[1]),
                          int(i.split(", ")[2].replace(")",""))) for i in df_rgb]
    
    df = pd.DataFrame(zip(df_color_up, df_percent), columns = ['c_code','occurence'])
    return df

df_color = color_to_df(colors_x)
df_color
print(df_color)
