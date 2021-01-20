.PHONY: all build clean info help

CXX        := -c++
INCLUDE    := -Iinclude/
INC        := $(INCLUDE)
CXXFLAGS   := -pedantic-errors -Wall -Wextra -Werror -O3 $(INC)
LDFLAGS    := -L/usr/lib -lstdc++ -lm
SRC        := $(wildcard *.cc)

OBJECTS    := $(SRC:%.cc=%.o)
TARGETS    := $(SRC:%.cc=%.x)

OBJ_DIR    := ./build
BUILD_DIR  := $(OBJ_DIR)/bin

all: build $(TARGETS)

help: info

info:
	@echo "[*] Object dir:      $(OBJ_DIR)     "
	@echo "[*] Build dir:       $(BUILD_DIR)   "
	@echo "[*] Sources:         ${SRC}         "
	@echo "[*] Objects:         ${OBJECTS}     "
	@echo "[*] Targets:         $(TARGETS)     "

build:
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(BUILD_DIR)

%.x: %.o
	@echo "Compiling $@."
	@$(CXX) $^ $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) -o $@
	@mv $^ $(OBJ_DIR)/$^
	@mv $@ $(BUILD_DIR)/$@

%: %.x
	@echo "Executing $@."
	@echo ""
	@echo "======================== stdout =========================="
	@./$(BUILD_DIR)/$@.x
	@echo "=========================================================="

clean:
	@rm -f *.o *.x
