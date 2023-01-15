def print_nums(cutoff):
    _print_nums(1, cutoff)

def _print_nums(current, cutoff):
    if current > cutoff: 
        return
    
    print(current)
    _print_nums(current + 1, cutoff)

def main():
    print_nums(int(input("enter positive integer: ")))

if __name__ == "__main__":
    main()