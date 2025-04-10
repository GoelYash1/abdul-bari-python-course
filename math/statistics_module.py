import statistics

data1 = [1,2,3,4,5]
print(data1)

print("Mean:",statistics.mean(data1))
print("Harmonic Mean:",statistics.harmonic_mean(data1))

data2 = [1,2,90,30,40,70]
print(data2)
print("Median Low:",statistics.median_low(data2))
print("Median:",statistics.median(data2))
print("Median High:",statistics.median_high(data2))

data3 = [1,2,1,2,3,1,2,3,4,1]
print(data3)
print("Mode:",statistics.mode(data3))

print(data1)
print(f"Population Standard Deviance: {statistics.pstdev(data1)}")
print(f"Standard Deviance: {statistics.stdev(data1)}")
print(f"Population Variance: {statistics.pvariance(data1)}")
print(f"Variance: {statistics.variance(data1)}")
