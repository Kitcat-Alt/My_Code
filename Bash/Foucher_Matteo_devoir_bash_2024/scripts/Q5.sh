#!/bin/bash
declare -A dictionnaire
for fichier in $(find ./ -type f); do
    if file "$fichier" | grep -qE 'image|bitmap'; then
        empreinte=$(shasum "$fichier" | awk '{print $1}')
        dictionnaire["$fichier"]=$empreinte
    fi
done
for fichier in "${!dictionnaire[@]}"; do
    echo "$fichier:${dictionnaire[$fichier]}"
done
