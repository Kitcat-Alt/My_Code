#!/bin/bash
num=0
rm -r Outputs
mkdir -p Outputs
find . -type f -iname "*.jpg" -exec shasum {} \; | awk '{print $2 ":" $1}' > empreintes.txt
cat empreintes.txt | awk -F ':' '{print $1}' | awk -F '/' '{print $NF}' | awk '{print substr($1, 1, 3)}' > stock.txt
while IFS= read -r line && IFS= read -r file <&3; do
    cp "$file" "Outputs/fichier_${line}_num_${num}.jpg"
    num=$((num+1))
done < stock.txt 3< <(find . -type f -iname "*.jpg")
find . -type f -iname "*.png" -exec shasum {} \; | awk '{print $2 ":" $1}' > empreintes.txt
cat empreintes.txt | awk -F ':' '{print $1}' | awk -F '/' '{print $NF}' | awk '{print substr($1, 1, 3)}' > stock.txt
while IFS= read -r line && IFS= read -r file <&3; do
    cp "$file" "Outputs/fichier_${line}_num_${num}.png"
    num=$((num+1))
done < stock.txt 3< <(find . -type f -iname "*.png")
find . -type f -iname "*.tif" -exec shasum {} \; | awk '{print $2 ":" $1}' > empreintes.txt
cat empreintes.txt | awk -F ':' '{print $1}' | awk -F '/' '{print $NF}' | awk '{print substr($1, 1, 3)}' > stock.txt
while IFS= read -r line && IFS= read -r file <&3; do
    cp "$file" "Outputs/fichier_${line}_num_${num}.tif"
    num=$((num+1))
done < stock.txt 3< <(find . -type f -iname "*.tif")
find . -type f -iname "*.bmp" -exec shasum {} \; | awk '{print $2 ":" $1}' > empreintes.txt
cat empreintes.txt | awk -F ':' '{print $1}' | awk -F '/' '{print $NF}' | awk '{print substr($1, 1, 3)}' > stock.txt
while IFS= read -r line && IFS= read -r file <&3; do
    cp "$file" "Outputs/fichier_${line}_num_${num}.bmp"
    num=$((num+1))
done < stock.txt 3< <(find . -type f -iname "*.bmp")
