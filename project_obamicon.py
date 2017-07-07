from PIL import Image

# RGB values for recoloring.
darkBlue = (0,0,0)
red = (128,0,0)
lightBlue = (0,128,128)
yellow =  (0,255,255) 


# Import image.
my_image = Image.open("uncolored.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.


recolored = []

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.
def pixel():
    for pix in image_list:
        RGB = pix[0] + pix[1] + pix [2]
        if RGB >= 182 and RGB < 364:
            recolored.append(red)
        elif RGB < 182:
            recolored.append(darkBlue)
        elif RGB >= 364 and RGB < 546:
            recolored.append(lightBlue)
        elif RGB >= 546:
            recolored.append(yellow)


# Create a new image using the recolored list. Display and save the image.
pixel()
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"

print(new_image)
