import ascii_magic
Ascci = ascii_magic.from_image_file(r"Path_Of_The_Image_You_Want_To_Convert_to_Ascii",columns=100,char="#")
ascii_magic.to_terminal(Ascci)
