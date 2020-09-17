# -*- coding: utf-8 -*-


import xml.etree.ElementTree as ET
import random
import os

TRAINNING_DATA_DIR = "./corpus/i2b2/2012-07-15.original-annotation.release/"
TEST_DATA_DIR = "./corpus/i2b2/ground_truth/merged_xml/"
SAVE_DIR = "./corpus/i2b2/"

def file_name(file_dir):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.xml':
                # L.append(os.path.join(root, file))
                L.append(file)
    return L


def data_process(inDIR, outFile):
    fileList = file_name(inDIR)
    print(len(fileList))
    lableType = set()
    outFile = open(outFile, "w")
    for f in fileList:
        print(f, end=' ')
        linkNO = 0
        inFile = open(inDIR + f, "r")
        xmlString = ""
        for lines in inFile.readlines():
            xmlString += lines.replace(" & ", " ").replace("&", " and ")
        inFile.close()

        parser = ET.XMLParser(encoding="utf-8")
        root = ET.fromstring(xmlString, parser=parser)
        # tree = ET.parse(inDIR + f)
        # root = tree.getroot()
        text = root.find("TEXT").text.replace("\n", " ").strip()
        # print(text)
        tags = root.find("TAGS")
        for tlink in tags.findall("TLINK"):
            id = f[:-4] +"_"+ str(tlink.attrib['id'] )
            target = tlink.attrib['fromText'] + " " + tlink.attrib['toText']
            label = tlink.attrib['type'].upper()
            if label == '':
                continue
            lableType.add(label)
            # print(id + "\t"+target + "\t" + label)
            outFile.write(id + "\t" + target + "\t" + text + "\t"+ label+"\n")
            linkNO += 1
        print("linkNO = " + str(linkNO))
    print("*"*80)
    
if __name__ == '__main__':
    data_process( TRAINNING_DATA_DIR , SAVE_DIR + "train.txt")
    data_process( TEST_DATA_DIR, SAVE_DIR + "test.txt")
    