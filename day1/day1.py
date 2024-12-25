import sys
    
loc1 = []
loc2 = []
loc_counts = {}

def get_nums(line):
    line_nums = [int(num) for num in line.split()]
    loc1.append(line_nums[0])
    loc2.append(line_nums[1])

def get_distance(left_loc, right_loc):
    return abs(left_loc - right_loc)

def count_appearance():
    for num in loc2: 
        loc_counts[num] = loc_counts.get(num, 0) + 1

def main(filename):
    try:
        with open(filename, 'r') as file:
            line = file.readline()
            while line:
                get_nums(line)
                line = file.readline()

            # part 1 
            # time complexity: O(nlogn) for sorting
            loc1.sort()
            loc2.sort()

            loc_sum = 0
            for i in range(len(loc1)):
                loc_sum += get_distance(loc1[i], loc2[i])

            print(f"Total distance: {loc_sum}")

            # part 2
            # time complexity: O(n)
            count_appearance()
            sim_score = 0
            for num in loc1: 
                sim_score += num * (loc_counts.get(num, 0))

            print(f"Similarity Score: {sim_score}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python day1.py <filename>")
    else:
        main(sys.argv[1])