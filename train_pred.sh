#!/bin/bash

#Train models with the best char-level hyper param, then get predictions for the test data for evaluation

#Gitksan unmerged
python3 main.py --language Gitksan --track 1 --batch 2 --dropout 0.3167482728780582 --hidden 368 --layers 1 --gamma 0.9958845808160292
#Gitksan merged
python3 main.py --language Gitksan --track 1 --merged --batch 2 --dropout 0.3167482728780582 --hidden 368 --layers 1 --gamma 0.9958845808160292
#Arapaho unmerged
python3 main.py --language Arapaho --track 1 --batch 90 --dropout 0.4521295443315911 --hidden 440 --layers 2 --gamma 0.9422354132655092
#Arapaho merged
python3 main.py --language Arapaho --track 1 --merged --batch 90 --dropout 0.4521295443315911 --hidden 440 --layers 2 --gamma 0.9422354132655092
#Lezgi unmerged
python3 main.py --language Lezgi --track 1 --batch 2 --dropout 0.1664142542782741 --hidden 122 --layers 1 --gamma 0.976565642756414
#Lezgi merged
python3 main.py --language Lezgi --track 1 --merged --batch 2 --dropout 0.1664142542782741 --hidden 122 --layers 1 --gamma 0.976565642756414
#Natugu unmerged
python3 main.py --language Natugu --track 1 --batch 36 --dropout 0.0009265620235793 --hidden 102 --layers 1 --gamma 0.9997553835382564
#Natugu merged
python3 main.py --language Natugu --track 1 --merged --batch 36 --dropout 0.0009265620235793 --hidden 102 --layers 1 --gamma 0.9997553835382564
#Nyangbo unmerged
python3 main.py --language Nyangbo --track 1 --batch 37 --dropout 0.1896144653956691 --hidden 425 --layers 2 --gamma 0.9449798769606876
#Nyangbo merged
python3 main.py --language Nyangbo --track 1 --merged --batch 37 --dropout 0.1896144653956691 --hidden 425 --layers 2 --gamma 0.9449798769606876
#Tsez unmerged
python3 main.py --language Tsez --track 1 --batch 28 --dropout 0.0239858083378134 --hidden 414 --layers 2 --gamma 0.9533363411113386
#Tsez merged
python3 main.py --language Tsez --track 1 --merged --batch 28 --dropout 0.0239858083378134 --hidden 414 --layers 2 --gamma 0.9533363411113386
#Uspanteko unmerged
python3 main.py --language Uspanteko --track 1 --batch 55 --dropout 0.3296004130093379 --hidden 370 --layers 2 --gamma 0.9594212206017776
#Uspanteko merged
python3 main.py --language Uspanteko --track 1 --merged --batch 55 --dropout 0.3296004130093379 --hidden 370 --layers 2 --gamma 0.9594212206017776