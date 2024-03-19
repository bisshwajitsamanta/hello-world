import os

# Get the Input and convert it to int
num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit(f'ERROR: The INPUT_NUM provided {num} is not an integer ')
else:
    num =1

print(f'::set-output name=num_squared::{num **2}')