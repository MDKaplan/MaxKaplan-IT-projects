

import sys

def instruction():
    print("Usage: python3 pa01.py <inputFilename.txt> <checksumSize>", file=sys.stderr)
    
    sys.exit(1)

def main():
    if len(sys.argv) != 3:
        instruction()

    file_name = sys.argv[1]

    try:
        checksum_size = int(sys.argv[2])

    except ValueError:
        print("Valid checksum sizes are 8, 16, or 32", file=sys.stderr)
        sys.exit(1)

    if checksum_size not in (8, 16, 32):
        print("Valid checksum sizes are 8, 16, or 32", file=sys.stderr)
        sys.exit(1)

    try:
       f = open(file_name, "rb")

    except FileNotFoundError:
        print(f"Error: file {file_name} not found", file=sys.stderr)
        sys.exit(1)

    data = f.read()
    f.close()

    char_count = len(data)

    text = data.decode("ascii", errors="replace")
    i = 0
    while i < len(text):
        print(text[i:i+80], end= "")

   
    bytes_p_group = checksum_size // 8

    pad_req = (bytes_p_group - (len(data) % bytes_p_group)) % bytes_p_group
    if pad_req > 0:
        data = data +(b"X" * pad_req)


    sumVal = 0

    if checksum_size == 8:
        for b in data:
            sumVal = sumVal + b
        checksum = sumVal & 0xFF

    elif checksum_size == 16:
        j = 0
        while j < len(data):
            two_bytes = (data[j] << 8) | data[j+1]
            sumVal = sumVal + two_bytes
            j += 2
            checksum = sumVal & 0xFFFF

    else:
        j = 0
        while j < len(data):
            four_bytes = (data[j] << 24) | (data[j+1] << 16) | (data[j+2] <<8) | data[j+3]
            sumVal = sumVal + four_bytes
            j += 4
        checksum = sumVal & 0xFFFFFFFF
        


    print(f"\n{checksum_size:2d} bit checksum is {checksum:08x} for all {char_count:4d} chars")

if __name__ == "__main__":
    main()

#=============================================================================
# I Max Kaplan(ma234101) affirm that this program is
# entirely my own work and that I have neither developed my code together with
# any another person, nor copied any code from any other person, nor permitted
# my code to be copied or otherwise used by any other person, nor have I
# copied, modified, or otherwise used programs created by others. I acknowledge
# that any violation of the above terms will be treated as academic dishonesty.
#=============================================================================