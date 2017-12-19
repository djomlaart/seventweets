.PHONY: clean list


index.html: README.md
	pandoc --template=styles/template.html  \
	       --from markdown --to html        \
	       --toc                            \
	       -o index.html README.md

clean:
	rm -f index.html
