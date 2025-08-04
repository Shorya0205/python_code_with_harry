#WAP to generate a multiplication table from 1 to 10 and write it to different files and store them in a folder
import os
def generate_multiplication_tables(n):
    table=""
    for i in range(1, 11):
        table += f"{n} x {i} = {n * i}\n"
       
    with open(f"tables/table_{n}.txt", "w") as file:
        file.write(table)


for i in range(1, 11):
    generate_multiplication_tables(i)


   