# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 01:09:42 2020

@author: dennis
"""

import numpy as np
import math

class Image:
    
    def __init__(self, img, id_):
        self.id = id_
        self.img = img
        self.neighbours = set()
        self.cunstruct_all_versions()

    def cunstruct_all_versions(self):
        self.versions = []
        for rot in range(4):
            for flip in range(2):
                modified_image = np.rot90(self.img, rot)
                if flip:
                    modified_image = np.flipud(modified_image)
                self.versions.append(modified_image)
        

def test_all_edges(t1, t2):
    if np.array_equal(t1[:,9], t2[:,0]):
        return 'right'
    elif np.array_equal(t1[:,0], t2[:,9]):
        return 'left'
    elif np.array_equal(t1[0,:], t2[9,:]):
        return 'up'
    elif np.array_equal(t1[9,:], t2[0,:]):
        return 'down'
    return False

# Process input
lines = open('data/20.txt').read().splitlines()
images = dict()
img = []
for line in lines:
    if len(line.split()) == 2:
        id_ = int(line.split()[-1][:-1])
    elif not line:
        img = np.uint8(img)
        images[id_] = Image(img, id_)
        img = []
    else:
        img.append([1 if x == '#' else 0 for x in line])

# Find neighbouring tiles
for img1 in images.values():
    for img2 in images.values():
        if img1.id == img2.id:
            continue
        elif len(img2.neighbours) == 4:
            continue
        for t1 in img1.versions:
            res = test_all_edges(t1, img2.img)
            if res:
                img1.neighbours.add(img2.id)
                img2.neighbours.add(img1.id)
                break
            if res:
                break
        if len(img1.neighbours) == 4:
            break
corners = [img.id for img in images.values() if len(img.neighbours) == 2]
print('Part 1:', math.prod(corners))

# Construct image from tiles
satellite_image = Image(np.zeros((96, 96), np.uint8), 0)
tracker = [[dict() for _ in range(12)] for _ in range(12)]
monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ']
monster = [[1 if x == '#' else 0 for x in line] for line in monster]
monster = np.uint8(monster)

# Choose random corner tile as top left and find correct versions of it's neighbours
def fill_satellite_image(s_img, img, x, y):
    img = img[1:-1, 1:-1]
    s_img.img[y*8:y*8+8, x*8:x*8+8] = img
    return s_img

top_left = images[corners[0]]
n1 = images[list(top_left.neighbours)[0]]
n2 = images[list(top_left.neighbours)[1]]
found = False
for img1 in top_left.versions:
    for img2 in n1.versions:
        for img3 in n2.versions:
            res1 = test_all_edges(img1, img2)
            res2 = test_all_edges(img1, img3)
            if (res1 == 'down' and res2 == 'right') or (res1 == 'right' and res2 == 'down'):
                found = True
                break
        if found:
            break
    if found:
        break
satellite_image = fill_satellite_image(satellite_image, img1, 0, 0)
tracker[0][0]['tile'] = img1
tracker[0][0]['id'] = top_left.id
if res1 == 'right':
    satellite_image = fill_satellite_image(satellite_image, img2, 1, 0)
    tracker[0][1]['tile'] = img2
    tracker[0][1]['id'] = n1.id
elif res2 == 'right':
    satellite_image = fill_satellite_image(satellite_image, img3, 1, 0)
    tracker[0][1]['tile'] = img3
    tracker[0][1]['id'] = n2.id

# Then build top row by finding the next tile to the right
def find_version(t1, img2, direction):
    for t2 in img2.versions:
        res = test_all_edges(t1, t2)
        if res == direction:
            return t2
    return False

for i in range(2, 12):
    t1 = tracker[0][i-1]['tile']
    for img_id in images[tracker[0][i-1]['id']].neighbours:
        img = images[img_id]
        res = find_version(t1, img, 'right')
        if np.any(res):
            satellite_image = fill_satellite_image(satellite_image, res, i, 0)
            tracker[0][i]['tile'] = res
            tracker[0][i]['id'] = img.id
            break

# Then build rows 2 - 12 by using the row above and complete the satellite image
for row in range(1, 12):
    for column in range(0, 12):
        t1 = tracker[row-1][column]['tile']
        for img_id in images[tracker[row-1][column]['id']].neighbours:
            img = images[img_id]
            res = find_version(t1, img, 'down')
            if np.any(res):
                satellite_image = fill_satellite_image(satellite_image, res, column, row)
                tracker[row][column]['tile'] = res
                tracker[row][column]['id'] = img.id
                break
satellite_image.cunstruct_all_versions()

# Find image with seamonsters
def find_monsters(img):
    img = img.copy()
    found = False
    for x in range(img.shape[1]-monster.shape[1]+1):
        for y in range(img.shape[0]-monster.shape[0]+1):
            section = img[y:y+monster.shape[0], x:x+monster.shape[1]]
            count = len(np.where(monster & (section == 1))[0])
            if count == np.sum(monster): # If monster found set all elements part of monster to 0
                found = True
                for i, row in enumerate(monster):
                    for j, e in enumerate(row):
                        if e and section[i, j]:
                            img[y+i, x+j] = 0
    if found:
        return img
    else:
        return False

for img in satellite_image.versions:
    found = find_monsters(img)
    if np.any(found):
        print('Part 2:', np.sum(found))
        break
