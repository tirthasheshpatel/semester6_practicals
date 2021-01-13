.PHONY: all build clean info

CXX        := -c++
CXXFLAGS   := -pedantic-errors -Wall -Wextra -Werror -O3
LDFLAGS    := -L/usr/lib -lstdc++ -lm
INCLUDE    := -Iinclude/
SRC        := $(wildcard *.cc)

OBJECTS    := $(SRC:%.cc=%.o)
TARGETS    := $(SRC:%.cc=%.x)

OBJ_DIR    := ./build
BUILD_DIR  := $(OBJ_DIR)

all: build $(TARGETS)

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
	@$(CXX) $^ $(CXXFLAGS) $(INCLUDE) -o $@
	@mv $^ $(OBJ_DIR)/$^
	@mv $@ $(BUILD_DIR)/$@

%: %.x
	@echo "Executing $@."
	@./$(BUILD_DIR)/$@.x

clean:
	@rm -f *.o *.x
