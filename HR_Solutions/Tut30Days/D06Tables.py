if __name__ == "__main__":
    n = int(input())
    for i in range(1,11): 
        # Using string concatenation:
        # print(n, ' x ', i, ' = ', ' ', n * i)
        


        # Using print f strings:
        # print(f"{n} x {i} = {n * i}")

        # With right-alignment formatting(best for readers clarity and neatness ):
        # print(f"{n:>3} x {i:<2} = {n*i:>4}")

        # With centered formatting:
        # print(f"{n:^5} x {i:^3} = {n*i:^6}")
        
        # With dividers/separators:
        # print(f"│ {n:>3} │ {i:<2} │ {n*i:>4} │")

        # Adding headers and dividers for better readability:
        # Table header version:
        # print("NUM x MUL = RESULT")
        # print("─" * 20)
        # for i in range(1, 11):
        # print(f"{n:>3} x {i:<2} = {n*i:>4}")

        # With centered formatting and dividers:
        # print(f"{n} × {i} = {n*i}".center(20))
    

        # Professional table format (using formatting):
        print(f"{n:5d} × {i:2d} = {n*i:5d}")
        
