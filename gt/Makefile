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

COLS       := `tput cols`
TWO        := 2
FOUR       := 4
CHARS_TMP  := $(shell expr $(COLS)/$(TWO))
CHARS      := $(shell expr $(CHARS_TMP)-$(FOUR))

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

%.x: $(BUILD_DIR)/%.x

%: $(BUILD_DIR)/%.x
	@SHELL=/bin/bash
	@echo "Executing $@."
	@echo ""
	@for i in seq 1, $(CHARS) ; do \
		echo -n "=" ; \
	done
	@echo -n " stdout "
	@for i in seq 1, $(CHARS) ; do \
		echo -n "=" ; \
	done
	@echo "\n"
	@./$(BUILD_DIR)/$@.x
	@echo "\n"
	@for i in seq 1, $(COLS) ; do \
		echo -n "=" ; \
	done
	@echo ""

clean:
	@rm -f *.o *.x
