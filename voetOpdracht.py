{\rtf1\ansi\ansicpg1252\cocoartf2708
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red39\green40\blue50;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c20392\c20784\c25490;\cssrgb\c100000\c100000\c100000;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
# coding=utf-8\
from mrjob.job import MRJob\
\
class AvgValueByFoot(MRJob):\
\
    def mapper(self, _, line):\
        # split the CSV line into an array of individual columns\
        columns = line.split(',')\
\
        # extract the value column and remove any currency symbols\
        value_str = columns[11].replace('\'80', '').replace('M', '000000').replace('K',$\
\
        # check if the value is 0 and skip the record\
        if value_str == '0':\
            return\
\
        # extract the preferred foot column and remove any single quotes\
        foot_str = columns[14].replace("'", "")\
\
        try:\
            # convert value to integer\
            value = int(value_str)\
            yield foot_str, (value, 1)\
        except ValueError:\
           # if the value cannot be converted to an integer, skip the record\
            pass\
\
    def combiner(self, foot, values):\
        total_value = 0\
        num_players = 0\
        for value, count in values:\
            total_value += value\
            num_players += count\
        yield foot, (total_value, num_players)\
\
    def reducer(self, foot, values):\
        total_value = 0\
        num_players = 0\
        for value, count in values:\
            total_value += value\
            num_players += count\
        avg_value = total_value / num_players\
        yield foot, avg_value\
\
if __name__ == '__main__':\
    AvgValueByFoot.run()}