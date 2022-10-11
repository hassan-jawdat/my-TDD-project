def sonar_sweep(input_file) -> int:
    with open(input_file, "r") as f:
        data = f.readlines()
        # Remove the newline character
        data = [x.strip() for x in data]
        # Convert to a list of floats
        data = [float(x) for x in data]
        # Count the number of measurements that are larger than the previous measurement
        count = 0
        for i in range(1, len(data)):
            if data[i] > data[i - 1]:
                count += 1
        return count


if __name__ == "__main__":
    print(sonar_sweep("input_orginal.txt")) 