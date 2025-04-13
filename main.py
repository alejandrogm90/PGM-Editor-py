#! /usr/bin/env python3

import os, sys
from clases.Image import Image, PIXEL_SPLIT


def load_image(file_path: str):
    """
    Read image file

    :param file_path: file path
    :return new_img1
    """
    f1 = open(file_path, "rb")
    tipo = str(f1.readline()).split("'")[1].split("\\")[0]
    des = str(f1.readline()).split("'")[1].split("\\")[0]
    cad = str(f1.readline()).split("'")[1].split("\\")[0]
    rows = int(cad.split(" ")[0])
    columns = int(cad.split(" ")[1])
    current_vector: list = [None] * (rows * columns)
    img1 = Image(type=tipo, path=file_path, comment=des, rows=rows, columns=columns, vector=current_vector)
    # To read file size pixels
    size_pixels = str(f1.readline())
    num = 0
    current_pos = 0
    while current_pos != (rows * columns):
        cad = str(f1.read(1)).split("'")[1].split("\\")[0]
        if cad != "":
            num = (num * 10) + int(cad)
        else:
            img1.set_pixel_pos(current_pos, int(num))
            num = 0
            current_pos += 1

    f1.close()
    return img1


def negative(img1: Image) -> Image:
    """
    Create an negative image
    """
    new_img1 = img1.__copy__()
    new_img1.path = new_img1.path.replace(".pgm", "_negative.pgm")
    for ff in range(0, (new_img1.rows * new_img1.columns)):
        new_img1.set_pixel_pos(ff, (255 - new_img1.get_pixel_pos(ff)))
    return new_img1


def inverse(img1: Image) -> Image:
    """
    Create an inverse image
    """
    new_img1 = img1.__copy__()
    new_img1.path = new_img1.path.replace(".pgm", "_inverse.pgm")
    for current_row in range(0, new_img1.rows):
        for current_column in range(0, int(new_img1.columns / 2)):
            diff_pos = new_img1.columns - current_column - 1
            left_pixel = new_img1.get_pixel(current_row, current_column)
            right_pixel = new_img1.get_pixel(current_row, diff_pos)
            new_img1.set_pixel(current_row, current_column, right_pixel)
            new_img1.set_pixel(current_row, diff_pos, left_pixel)
    return new_img1


def transpose(img1: Image) -> Image:
    """
    Create an image transpose
    """
    new_img1 = img1.__copy__()
    new_img1.path = new_img1.path.replace(".pgm", "_transpose.pgm")
    num_pixel_total = int((new_img1.rows * new_img1.columns) / 2) + int(new_img1.columns / 2)
    for new_pixel_pos in range(0, num_pixel_total):
        old_pixel_pos = new_img1.rows - new_pixel_pos
        pix_antiguo = new_img1.get_pixel_pos(new_pixel_pos)
        pix_nuevo = new_img1.get_pixel_pos(old_pixel_pos)
        new_img1.set_pixel_pos(new_pixel_pos, pix_nuevo)
        new_img1.set_pixel_pos(old_pixel_pos, pix_antiguo)
    return new_img1


def codificate(img1: Image, text1: str) -> Image:
    """
    Create codificate text in an image

    :param img1: Image object
    :param text1: text to codificate
    """
    new_img1 = img1.__copy__()
    new_img1.path = new_img1.path.replace(".pgm", "_codificate.pgm")
    num_pixel_total = int((new_img1.rows * new_img1.columns) / 2) - 1
    num_letras_total = len(text1)
    pos_en_texto = 0
    img_pos = 0
    while (img_pos + PIXEL_SPLIT) < num_pixel_total and pos_en_texto <= num_letras_total:
        if pos_en_texto != num_letras_total:
            new_img1.set_pixel_pos(img_pos, ord(text1[pos_en_texto]))
        else:
            new_img1.set_pixel_pos(img_pos, 254)
        pos_en_texto = pos_en_texto + 1
        img_pos = img_pos + PIXEL_SPLIT
    return new_img1


def decodify(img1: Image) -> None:
    """
    Create decodify text in an image
    """
    new_img1 = img1.__copy__()
    num_pixel_total = int((new_img1.rows * new_img1.columns) / 2) - 1
    texto_final = ""
    letra = 0
    img_pos = 0
    while letra != 254 and img_pos < num_pixel_total:
        letra = new_img1.get_pixel_pos(img_pos)
        texto_final = texto_final + chr(letra)
        img_pos = img_pos + PIXEL_SPLIT
    # print text
    print_text_in_file(new_img1.path.replace(".pgm", "_decodify.pgm"), texto_final)


def print_text_in_file(file_path: str, texto_final: str) -> None:
    """
    Print text in file
    """
    f1 = open(file_path, "w")
    for line in texto_final.split("', '"):
        line2 = line
        # Strat chars in file
        if line2[0:2] == "['":
            line2 = line2[2:len(line2)]
        # Last chars in file
        if line2[len(line2) - 2:len(line2)] == "]þ":
            line2 = line2[0:len(line2) - 3]
        else:
            line2 = line2[0:len(line2) - 2]
        f1.write(line2 + "\n")
    f1.close()


def create_all(img1: Image) -> None:
    """
    Create an image inverse, other transpose and last inverse and transpose
    """
    img1.comment = "# Using Python3.3: PGM-Python"
    negative(img1).save()
    inverse(img1).save()
    transpose(img1).save()
    transpose(inverse(img1)).save()


def print_error() -> None:
    print(sys.argv[0] + " [ARGUMENT] [FILE-NAME] [FILE-TO-CODIFICATE *.txt]")
    print("ARGUMENTS: ")
    print(" --inverse, -i : Return the inverse of given file")
    print(" --transposed, -t : Return the transposed of given file")
    print(" --all, -a : Return both options (inverse and transposed) ")
    print(" --encode, -e : Encode text inside a PGM file")
    print(" --decode, -d : Return the text from a PGM file encoded")
    exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print_error()
    else:
        action = ""
        file_to_codificate = ""
        image1 = Image

        for element in sys.argv[1:]:
            print(element)
            if element.startswith("-"):
                action = element
            else:
                if os.path.exists(element):
                    if element.endswith(".pgm") or element.endswith(".PGM"):
                        image1 = load_image(element)
                    elif element.endswith(".txt"):
                        file_to_codificate = element
                else:
                    print(f"File {element} do not exists.")

        if action == "" or image1.path == "":
            print_error()
        else:
            if action == "--all" or action == "-a":
                create_all(image1)
            elif action == "--inverse" or action == "-i":
                inverse(image1).save()
            elif action == "--transpose" or action == "-t":
                transpose(image1).save()
            elif action == "--encode" or action == "-e":
                if len(sys.argv) == 4:
                    texto1 = str(open(sys.argv[3]).readlines())
                    codificate(image1, texto1).save()
                else:
                    print("A text file to insert in PGM image is required.")
            elif action == "--decode" or action == "-d":
                decodify(image1)
            else:
                print("No valid action has been found.")
                print_error()
