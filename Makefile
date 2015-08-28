all: build

build:
	./build.sh

clean:
	rm pex_uwsgi
	rm -rf uwsgi-*

.PHONY: all clean

