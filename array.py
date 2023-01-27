class data:
    def __init__(self) -> None:
        self.array = [0]*3

    def create_array(self):
        for i in range(3):
            self.array[i]=i
        return self.array

def main():
    struc = data()
    array = struc.create_array()
    print(array)

if __name__ == "__main__":
    main()
    
