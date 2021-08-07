import sys
import re


filename = "movie-names.txt"
filename2 = "movie-matrix.txt"

with open(filename) as f:
    lines = f.read().splitlines()

#print(lines)
numMovie = len(lines)
print("*** No. rows (movies) in matrix = " + str(len(lines)) )


movieMatrix = list()
with open("movie-matrix.txt","r") as f:
  Reviews = f.readlines()
for line in Reviews:
  mReview = line.strip()
  Rlist = mReview.split(";")
  finList = [int(r) if r!='' else 0 for r in Rlist]
  movieMatrix.append(finList)
  