SOURCE_DIR := ./src
BUILD_DIR := ./build

IPYNB_FILES := $(wildcard $(SOURCE_DIR)/*.ipynb)
IPYNB_MD_FILES := $(IPYNB_FILES:.ipynb=_ipynb.md)
MD_FILES := $(wildcard $(SOURCE_DIR)/*.md)
INCLUDE_FILES := $(shell find $(SOURCE_DIR)/include -type f -name '*' -print)

# The final build step
$(BUILD_DIR)/output.pdf: $(IPYNB_MD_FILES) $(MD_FILES) $(INCLUDE_FILES)
	mkdir -p "$(BUILD_DIR)"
	pandoc -s -f markdown --listings --pdf-engine=pdflatex --template eisvogel.latex \
	--lua-filter=include-code-files.lua \
	--resource-path="$(SOURCE_DIR)" -o "$@" $(sort $(IPYNB_MD_FILES) $(MD_FILES))

# Build step for ipynb files
%_ipynb.md: %.ipynb
	jupyter nbconvert --execute --to=markdown --output-dir="$(dir $@)" --output="$(shell basename $@ .md)" "$<"

# Live reload
.PHONY: live
live:
	trap 'kill 0' EXIT; \
	python -m http.server 8000 & \
	watchexec --exts md,ipynb,tex make -j3 build/output.pdf & \
	wait

.PHONY: clean
clean:
	@if [ -z "$(BUILD_DIR)" ]; then \
		echo "Error: BUILD_DIR is not set."; \
		exit 1; \
	fi
	rm -rf "$(BUILD_DIR)"
	rm -f "$(SOURCE_DIR)"/*_ipynb.md
	rm -rf "$(SOURCE_DIR)"/*_ipynb_files

.SECONDARY:
