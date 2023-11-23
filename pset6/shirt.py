import sys, os
from PIL import Image, ImageOps

argc = len(sys.argv)

# check CLAs
if argc < 3:
    sys.exit("Too few command-line arguments")
elif argc > 3:
    sys.exit("Too many command-line arguments")
else:
    # check for extension conditionals
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    extlist = [".jpg", ".jpeg", ".png"]
    if not ext2 in extlist:
        sys.exit("Invalid output")
    elif not ext1 == ext2:
        sys.exit("Input and output have different extensions")
    else:
        try:
            # open shirt image and input image
            shirt = Image.open("shirt.png")
            original = Image.open(sys.argv[1])
            # get size of shirt image
            shirt_size = shirt.size
            # resize input image to match shirt image size
            output = ImageOps.fit(original, shirt_size)
            # overlay shirt image on top of resized output image
            # second "shirt" represents a “mask” indicating which pixels in output to update
            output.paste(shirt, shirt)
            # save output as name in CLA
            output.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Input does not exist")