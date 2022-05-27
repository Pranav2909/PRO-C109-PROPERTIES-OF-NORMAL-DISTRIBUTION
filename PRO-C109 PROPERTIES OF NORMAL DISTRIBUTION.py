import pandas as pd
import statistics

df = pd.read_csv("StudentsPerformance.csv")
mathScore_list = df["math score"].to_list()
readingScore_list = df["reading score"].to_list()
writingScore_list = df["writing score"].to_list()

mathScore_mean = statistics.mean(mathScore_list)
readingScore_mean = statistics.mean(readingScore_list)
writingScore_mean = statistics.mean(writingScore_list)

mathScore_median = statistics.median(mathScore_list)
readingScore_median = statistics.median(readingScore_list)
writingScore_median = statistics.median(writingScore_list)

print("Mean, Median of math score is {}, {}  respectively".format(mathScore_mean, mathScore_median))
print("Mean, Median of reading score is {}, {}  respectively".format(readingScore_mean, readingScore_median))
print("Mean, Median of writing score is {}, {}  respectively".format(writingScore_mean, writingScore_median))

mathScore_std_deviation = statistics.stdev(mathScore_list)
readingScore_std_deviation = statistics.stdev(readingScore_list)
writingScore_std_deviation = statistics.stdev(writingScore_list)

mathScore_first_std_deviation_start, mathScore_first_std_deviation_end = mathScore_mean-mathScore_std_deviation, mathScore_mean+mathScore_std_deviation
mathScore_second_std_deviation_start, mathScore_second_std_deviation_end = mathScore_mean-(2*mathScore_std_deviation), mathScore_mean+(2*mathScore_std_deviation)
mathScore_third_std_deviation_start, mathScore_third_std_deviation_end = mathScore_mean-(3*mathScore_std_deviation), mathScore_mean+(3*mathScore_std_deviation)

readingScore_first_std_deviation_start, readingScore_first_std_deviation_end = readingScore_mean-readingScore_std_deviation, readingScore_mean+readingScore_std_deviation
readingScore_second_std_deviation_start, readingScore_second_std_deviation_end = readingScore_mean-(2*readingScore_std_deviation), readingScore_mean+(2*readingScore_std_deviation)
readingScore_third_std_deviation_start, readingScore_third_std_deviation_end = readingScore_mean-(3*readingScore_std_deviation), readingScore_mean+(3*readingScore_std_deviation)

writingScore_first_std_deviation_start, writingScore_first_std_deviation_end = writingScore_mean-writingScore_std_deviation, writingScore_mean+writingScore_std_deviation
writingScore_second_std_deviation_start, writingScore_second_std_deviation_end = writingScore_mean-(2*writingScore_std_deviation), writingScore_mean+(2*writingScore_std_deviation)
writingScore_third_std_deviation_start, writingScore_third_std_deviation_end = writingScore_mean-(3*writingScore_std_deviation), writingScore_mean+(3*writingScore_std_deviation)

mathScore_list_of_data_within_1_std_deviation = [result for result in mathScore_list if result > mathScore_first_std_deviation_start and result < mathScore_first_std_deviation_end]
mathScore_list_of_data_within_2_std_deviation = [result for result in mathScore_list if result > mathScore_second_std_deviation_start and result < mathScore_second_std_deviation_end]
mathScore_list_of_data_within_3_std_deviation = [result for result in mathScore_list if result > mathScore_third_std_deviation_start and result < mathScore_third_std_deviation_end]

readingScore_list_of_data_within_1_std_deviation = [result for result in readingScore_list if result > readingScore_first_std_deviation_start and result < readingScore_first_std_deviation_end]
readingScore_list_of_data_within_2_std_deviation = [result for result in readingScore_list if result > readingScore_second_std_deviation_start and result < readingScore_second_std_deviation_end]
readingScore_list_of_data_within_3_std_deviation = [result for result in readingScore_list if result > readingScore_third_std_deviation_start and result < readingScore_third_std_deviation_end]

writingScore_list_of_data_within_1_std_deviation = [result for result in writingScore_list if result > writingScore_first_std_deviation_start and result < writingScore_first_std_deviation_end]
writingScore_list_of_data_within_2_std_deviation = [result for result in writingScore_list if result > writingScore_second_std_deviation_start and result < writingScore_second_std_deviation_end]
writingScore_list_of_data_within_3_std_deviation = [result for result in writingScore_list if result > writingScore_third_std_deviation_start and result < writingScore_third_std_deviation_end]

print("{}% of data for mathScore lies within 1 standard deviation".format(len(mathScore_list_of_data_within_1_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for mathScore lies within 2 standard deviations".format(len(mathScore_list_of_data_within_2_std_deviation)*100.0/len(mathScore_list)))
print("{}% of data for mathScore lies within 3 standard deviations".format(len(mathScore_list_of_data_within_3_std_deviation)*100.0/len(mathScore_list)))

print("{}% of data for readingScore lies within 1 standard deviation".format(len(readingScore_list_of_data_within_1_std_deviation)*100.0/len(readingScore_list)))
print("{}% of data for readingScore lies within 2 standard deviations".format(len(readingScore_list_of_data_within_2_std_deviation)*100.0/len(readingScore_list)))
print("{}% of data for readingScore lies within 3 standard deviations".format(len(readingScore_list_of_data_within_3_std_deviation)*100.0/len(readingScore_list)))

print("{}% of data for writingScore lies within 1 standard deviation".format(len(writingScore_list_of_data_within_1_std_deviation)*100.0/len(writingScore_list)))
print("{}% of data for writingScore lies within 2 standard deviations".format(len(writingScore_list_of_data_within_2_std_deviation)*100.0/len(writingScore_list)))
print("{}% of data for writingScore lies within 3 standard deviations".format(len(writingScore_list_of_data_within_3_std_deviation)*100.0/len(writingScore_list)))