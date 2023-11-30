def calculate_mean(data):
    total = sum(data)
    mean = total / len(data)
    return mean

def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
    else:
        median = sorted_data[n//2]
    return median

def calculate_mode(data):
    counts = {}
    for num in data:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    max_count = max(counts.values())
    mode = [num for num, count in counts.items() if count == max_count]
    return mode

# Example usage
data = [1, 2, 3, 4, 5, 5, 6, 6, 6, 7]
mean = calculate_mean(data)
median = calculate_median(data)
mode = calculate_mode(data)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
