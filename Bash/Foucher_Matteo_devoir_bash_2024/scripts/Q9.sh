#!/bin/bash
mkdir -p ImageRedim
input_dir="OutPut"
output_dir="ImageRedim"
find "$input_dir" -type f -iname "*.jpg" | while read -r file; do
	filename=$(basename "$file")
	output_path="$output_dir/$filename"
	convert "$file" -geometry 200x260^ -gravity center -crop 200x260+0+0 +repage "$output_path"
done
