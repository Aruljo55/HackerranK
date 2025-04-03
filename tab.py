import os

def taumBday(b, w, bc, wc, z):
    # Calculate the minimum cost using direct and conversion options
    min_black_cost = min(bc, wc + z)  # Buy black directly or convert white
    min_white_cost = min(wc, bc + z)  # Buy white directly or convert black
    
    return (b * min_black_cost) + (w * min_white_cost)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        b, w = map(int, input().split())
        bc, wc, z = map(int, input().split())

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
