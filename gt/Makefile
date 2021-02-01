.PHONY: all build clean info help

CXX        := -c++
PYTHON     := python
SHELL      := /bin/bash

INCLUDE    := -Iinclude/
INC        := $(INCLUDE)
CXXFLAGS   := -pedantic-errors -Wall -Wextra -Werror -O3 $(INC)
LDFLAGS    := -L/usr/lib -lstdc++ -lm

SRC        := $(wildcard *.cc)
OBJ_DIR    := ./build
BUILD_DIR  := $(OBJ_DIR)/bin

OBJECTS    := $(SRC:%.cc=%.o)
TARGETS    := $(SRC:%.cc=$(BUILD_DIR)/%.x)

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

$(BUILD_DIR)/%.x: %.o
	@echo "Compiling $@."
	@$(CXX) $^ $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) -o $@
	@mv $^ $(OBJ_DIR)/$^

%: build $(BUILD_DIR)/%.x
	@echo "Executing $@."
	@$(PYTHON) helper.py 0
	@./$(BUILD_DIR)/$@.x
	@$(PYTHON) helper.py 1

%.x: $(BUILD_DIR)/%.x

clean:
	@rm -rf build/*.o build/bin/*.x __pycache__/
