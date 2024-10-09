import random

#1. úkol list devítí čísel, který je přeházený
array=[65,69,32,87,21,78,15,39,52]
random.shuffle(array)
print (array)

#2. úkol první prostření a poslední  hodnota 
print(array[0])
print(array[int(len(array)/2)]) 
print(array[-1])

#3. úkol prostřední hodnota zaměněna za 34
array[int(len(array)/2)] = 34
print (array)

#4. úkol vypsáno 7 číslo
print(array[6])

#5. úkol delká pole
print(len(array))

#6. úkol min a max hodnota pole
print(min(array))
print(max(array))

#7. úkol druhé pole + bonus
array2=[69,61,28,94,25]
random.shuffle(array2)

#8. úkol součet pole 
print (array2 + array)

#9. úkol součet 1. a 5. indexu v druhém poli
array3 = array2[0] + array2[4]
print (array3)

