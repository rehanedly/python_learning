# Write a function that will take an array a paramenter and count the occrances of maximum number in the array

length_of_candles = [-2, -3, -4, -5, -6, -7, -7, -4, -5, -6, -7]
def calculate_number_max_coccurances(length_of_candles = []):
    
	if(not len(length_of_candles)):
		return 0;

	max_length = length_of_candles[0]
	max_length_occurances = 0

	for length_of_candle in length_of_candles:
		if(length_of_candle >  max_length):
			max_length = length_of_candle
			max_length_occurances = 1
		elif(max_length == length_of_candle):
			max_length_occurances += 1

	return max_length_occurances

result = calculate_number_max_coccurances(length_of_candles)
print(result)