__author__ = 'narendra'



import os, sys, glob
from PIL import Image

def image_resize(width, height):
    size = (width, height)
    input_dir = "/home/narendra/narendra_test/compress_images/input/"
    out_put_dir = "/home/narendra/narendra_test/compress_images/output/"
    for infile in os.listdir(input_dir):
        outfile = os.path.join(out_put_dir, infile)
        if infile != outfile    :
            try:
                im = Image.open(os.path.join(input_dir, infile))
                im1 = im.resize(size, Image.ANTIALIAS)
                im1.save(outfile)
                print "saved"
            except IOError as e:
                print "cannot create thumbnail for '%s'" % infile
            except Exception as e:
                print e



def open_rotate_display_image(image_path):
    im = Image.open(image_path)
    im.rotate(45).show()


def create_thumbnail(width, height):
    '''
    Working Fine for Creating thumbnails
    '''
    size = width, height
    for infile in glob.glob("*.jpg"):
        print infile
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(file + "_thumbnail" + ".JPEG")

def create_thumbnail_2(width, height):
    '''

    '''
    size = width, height
    input_dir = "/home/narendra/narendra_test/compress_images/input/"
    for infile in os.listdir(input_dir):
        print infile
        file, ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(file + "_thumbnail" + ".JPEG")


if __name__ == '__main__':
    # image_resize(50, 50)
    path = '/home/narendra/Desktop/potta.png'
    # open_rotate_display_image(path)
    # create_thumbnail(50,50)
    create_thumbnail_2(50,50)