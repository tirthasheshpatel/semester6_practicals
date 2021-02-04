.PHONY: all

SRC        := $(wildcard *.md)

TARGETS    := $(SRC:%.md=%)

all: $(TARGETS)

%:
	@echo "Creating '$@.pdf'"
	@pandoc $@.md --pdf-engine=xelatex -o 18BCE244_$@.pdf
