



# Couldn't complete Shortest Job First :(







def main():
    table = [
    #     ID ,AT, BT
        ["P1", 0, 10], 
        ["P2", 3,  4], 
        ["P3", 5,  8], 
        ["P4", 7, 13], 
        ["P5",10,  5]
    ]
    sjf(table)
    
def sjf(table):
    table.sort(key=lambda x: x[2])
    table = [x + [0 for i in range(3)] for x in table]
    
    
if __name__ == "__main__":
    main()