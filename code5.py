import math

def main():
    start = 0
    end = 2 * math.pi
    num_points = 1000

    step = (end - start) / (num_points - 1)

    print("     x\t\t   sin(x)")
    print("-" * 26)

    for i in range(num_points):
        x = start + i * step
        y = math.sin(x)
        print(f"{x:.6f}\t {y:.6f}")

if __name__ == "__main__":
    main()