import os
import cv2
import logging
logging.baseConfig(filename="log.log")
indirec='home/pipa1/Датасет ДЗ'
outdirec='home/pipa1/Датасет ДЗ'
files=os.listdir(indirec)
for i in files:
    f=os.listdir(i)
    for j in f:
        try:
        image = cv2.imread(indirec+i)
        image=cv2.resize(image,(128,128))
        cv2.imwrite(outdirec+i,image)
        logging.info("Удалось обработать изображение")
        except Exception:
        logging.warning("Не удалось обработать изображение")

