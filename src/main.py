import os

if __name__ == '__main__':
    img = "img.jpg"
    tool = "IMG_READ_SHOW_WRITE"
    os.system("python src/{}.py --image img/{}".format(tool, img))
