# Assignment 2
# -----------------
# converting coordinate

import argparse
import numpy as np
import cv2


def parse_args():
    parser = argparse.ArgumentParser(description='parser_init')
    execution_cfg = parser.add_mutually_exclusive_group()
    execution_cfg.add_argument('-i', '--imaginaryData',
                               action='store_true', help='run with imaginary data')
    execution_cfg.add_argument('-r', '--realData', action='store_true',
                               help='run with imaginary data')

    image_cfg = parser.add_mutually_exclusive_group()
    image_cfg.add_argument('-s', '--imageSize', type=int, nargs=2,
                           help='input each values of total # of rows & columns')
    image_cfg.add_argument('-d', '--directory',
                           help='directory to the input image')

    input_cfg = parser.add_mutually_exclusive_group()
    input_cfg.add_argument('-p', '--pixelCoordinate', type=int, nargs=2,
                           help='the location(row & col) of the point you wish to convert to image coordinate')
    input_cfg.add_argument(
        '-m', '--mouseClick', action='store_true', help='input the point location using click')

    parser.add_argument('-c', '--cameraSensorSize', type=float, nargs='+', default=1,
                        help='camera sensor size, (col_width, row_width) if different [um/pixel]')

    # parser.add_argument('-tc', '--totalColumns', type=int,
    #                     metavar='', required=True, help='total number of columns')
    # parser.add_argument('-tr', '--totalRows', type=int, metavar='',
    #                     required=True, help='total number of columns')

    args = parser.parse_args()
    if not (args.imaginaryData or args.realData):
        parser.error('No action requested, add -i or -r')
    if len(args.cameraSensorSize) > 2:
        parser.error('Camera sensor size should be given as 1D or')

    return args


def main(args):
    if args.imaginaryData:
        imageSize = np.array(args.imageSize)  # (#_of_row, #_of_col)
        pixelCoordinate = rangeChecker(
            imageSize, np.array(args.pixelCoordinate))

    elif args.realData:
        img = cv2.imread(args.directory)
        cv2.imshow('image', img)
        cv2.setMouseCallback('image', clickEvent)
        cv2.waitKey(0)

        imageSize = np.array(img.shape[:2])
        pixelCoordinate = np.array([mouseY, mouseX])

    imageCoordinate = pixel2image(imageSize, pixelCoordinate)
    photoCoordinate = image2photo(imageCoordinate, args.cameraSensorSize)
    print(photoCoordinate)


def rangeChecker(imageSize: np.ndarray, pixelCoordinate: np.ndarray):
    while np.min(imageSize-pixelCoordinate) < 1 or np.min(pixelCoordinate) < 0:
        print(
            "Your pixel of interest is not within the image {0}".format(imageSize))
        p_row = int(
            input("Enter new row value(0 ~ {0}): ".format(imageSize[0]-1)))
        p_col = int(
            input("Enter new column value(0 ~ {0}): ".format(imageSize[1]-1)))
        pixelCoordinate = np.array([p_row, p_col])
    return pixelCoordinate


def pixel2image(imageSize: np.ndarray, pixelCoordinate: np.ndarray):
    imageCoordinate = np.flip(
        (pixelCoordinate - (imageSize-1)/2)*np.array([-1, 1]))
    return imageCoordinate


def image2photo(imageCoordinate: np.ndarray, cameraSensorSize):
    photoCoordinate = imageCoordinate*np.array(cameraSensorSize)
    return photoCoordinate


def clickEvent(event, x, y, flags, params):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX, mouseY = x, y
        cv2.destroyAllWindows()


if __name__ == '__main__':
    args = parse_args()
    print(args)
    main(args)
