import csv
import inspect
import numpy as np
import cv2
import pandas as pd
from matplotlib import pyplot as plt
from Domain.Plant import Plant

from Domain.Pollen import Pollen


class ColorScan:
    def pollen_compare(self, pollen):
        inspect.isclass(Pollen)
        with open('..\CSV\pollenchart.csv', 'r', encoding="utf-8-sig") as csvDataFile:
            csv_reader = csv.DictReader(csvDataFile, delimiter=",")
            for row in csv_reader:
                rgb = {int(row['Red']), int(row['Green']), int(row['Blue'])}
                season = row['Season']
                if rgb == pollen.rgb and season == pollen.season:
                    return Plant(row['Plant name EN'])



colorScan = ColorScan()
print(ColorScan.pollen_compare(colorScan, Pollen(5, 5, 5)))
print(ColorScan.pollen_compare(colorScan, Pollen(171, 181, 101)))
