# %%
import cv2
from colorthief import ColorThief

# %%
camera=cv2.VideoCapture(0)

# %%
while True:
    _, image=camera.read()
    cv2.imshow('image', image)
    if cv2.waitKey(1)& 0xFF==ord('s'):
        cv2.imwrite('test1.jpg', image)
        break
camera.release()
cv2.destroyAllWindows()
def ss():
    ColorThief=ColorThief('test1.jpg')
    colors=ColorThief.get_pallete(color_count=2)
    print(colors)
ss()


