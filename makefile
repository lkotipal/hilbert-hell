#ZOLTAN = /home/lkotipal/Documents/Projects/Trilinos/packages/zoltan
#INCLUDE = -I$(ZOLTAN)/src/hsfc -I$(ZOLTAN)/src/zz -I$(ZOLTAN)/src/Utilities/shared -I$(ZOLTAN)/BUILD_DIR/src/include -I$(ZOLTAN)/src/include -I$(ZOLTAN)/src/lb -I$(ZOLTAN)/src/params -I$(ZOLTAN)/src/order -I$(ZOLTAN)/src/par -I$(ZOLTAN)/src/tpls
#OBJS = $(ZOLTAN)/BUILD_DIR/src/hsfc_hilbert.o
#CXXFLAGS = $(INCLUDE)

main: hsfc_hilbert.o main.cpp
	g++ $(CXXFLAGS) -o main main.cpp hsfc_hilbert.o

hsfc_hilbert.o: hsfc_hilbert.c hsfc_hilbert_const.h tables.h
	g++ $(CXXFLAGS) -o hsfc_hilbert.o -c hsfc_hilbert.c

clean:
	rm main hsfc_hilbert.o