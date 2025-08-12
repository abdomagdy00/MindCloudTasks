
from PIL import Image

myImage = Image.open("Image.jpg")
#Image Before Edit
myImage.show()


width, height = myImage.size

quarter_width = width // 4
quarter_height= height // 4

black_area = Image.new("RGB", (quarter_width, quarter_height), "black")
myImage.paste(black_area, (0, 0))
myImage.show()
myImage.save("AfterEdit.jpg")