PROG = app

OUT = out

SRC = src

FLAGS = -Wall -g -std=c++11

CC = g++

OBJS = $(SRC)/main.o $(SRC)/matrix.o

build: $(OBJS)
	mkdir -p $(OUT)
	$(CC) -o $(OUT)/$(PROG) $(OBJS)

main.o:
	$(CC) $(FLAGS) -c $(SRC)/main.cpp

matrix.o:
	$(CC) $(FLAGS) -c $(SRC)/matrix.cpp

clean:
	rm $(SRC)/*.o
	rm -rf $(OUT)

run:
	./$(OUT)/$(PROG)
