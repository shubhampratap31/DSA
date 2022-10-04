from PIL import Image
from PIL import ImageFilter


image=Image.open('i123.jpeg')
nmi=image.resize((700,700))


imageObject = Image.open("i123.jpeg");
sharpened1 = imageObject.filter(ImageFilter.SHARPEN);
sharpened2 = imageObject.filter(ImageFilter.SHARPEN);
sharpened3 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened4 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened5 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened6 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened7 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened8 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened9 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened10 = sharpened1.filter(ImageFilter.SHARPEN);
sharpened11= sharpened1.filter(ImageFilter.SHARPEN);

sharpened1.show();
# sharpened2.show();
# sharpened5.show();
sharpened11.show();
nmi.save('new_i123.jpeg')
