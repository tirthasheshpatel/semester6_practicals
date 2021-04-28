.PHONY: all build clean info help

CXX        := -c++
SHELL      := /bin/bash

INCLUDE    := -Iinclude/
INC        := $(INCLUDE)
CXXFLAGS   := -O3 $(INC)
LDFLAGS    := -L/usr/lib -lstdc++ -lm

SRC        := $(wildcard *.cc)
OBJ_DIR    := ./build
BUILD_DIR  := $(OBJ_DIR)/bin

OBJECTS    := $(SRC:%.cc=%.o)
TARGETS    := $(SRC:%.cc=$(BUILD_DIR)/%.x)

SUBMIT_DIR := ./submission_files
SUBMIT_SRC := $(wildcard $(SUBMIT_DIR)/*.md)
SUBMIT     := $(SUBMIT_SRC:$(SUBMIT_DIR)/%.md=%.pdf)

all: build $(TARGETS) $(SUBMIT)

help: info

info:
	@echo "[*] Object dir:      $(OBJ_DIR)     "
	@echo "[*] Build dir:       $(BUILD_DIR)   "
	@echo "[*] Submission dir:  $(SUBMIT_DIR)  "
	@echo "[*] Sources:         $(SRC)         "
	@echo "[*] Objects:         $(OBJECTS)     "
	@echo "[*] Targets:         $(TARGETS)     "
	@echo "[*] Submissions:     $(SUBMIT)      "

build:
	@mkdir -p $(OBJ_DIR)
	@mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/%.x: %.o
	@echo "Compiling $@."
	@$(CXX) $^ $(CXXFLAGS) $(INCLUDE) $(LDFLAGS) -o $@
	@mv $^ $(OBJ_DIR)/$^

%.x: $(BUILD_DIR)/%.x

%.pdf:
	@cd $(SUBMIT_DIR) ; $(MAKE) `echo $@ | grep -o '^[^\.]*'` --no-print-directory

%: build $(BUILD_DIR)/%.x
	@echo "Executing $@."
	@python3.9 helper.py 0
	@./$(BUILD_DIR)/$@.x
	@python3.9 helper.py 1

clean:
	@rm -rf build/*.o build/bin/*.x __pycache__/
