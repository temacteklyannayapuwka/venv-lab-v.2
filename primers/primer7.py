#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()
        # Вывод предложений с запятыми.
        for sentence in sentences:
            if "," in sentence:
                print(sentence)
