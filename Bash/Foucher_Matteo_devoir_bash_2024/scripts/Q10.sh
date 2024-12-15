#!/bin/bash
input_dir="ImageRedim"
output_image="mosaique.jpg"
montage "$input_dir"/*.jpg -tile 10x -geometry 100x130 "$output_image"
