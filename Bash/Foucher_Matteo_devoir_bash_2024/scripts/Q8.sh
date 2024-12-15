#!/bin/bash
mkdir -p OutPut
output_dir="OutPut"
num=0
find . -type f -iname "*jpg" -o -iname "*.gif" -o -iname "*.png" -o -iname "*.bmp" -o -iname "*.tif" | while read -r file; do
	if [[ -e "$file" ]]; then
	   filename=$(basename "$file")
	   prefixe="${filename:0:3}"
	   new_name="fichier_${prefixe}_num_${num}.jpg"
	   convert "$file" "$output_dir/$new_name"
	   num=$((num+1))
	fi
done
