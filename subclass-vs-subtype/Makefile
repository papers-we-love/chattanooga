oofun.html: oofun.org reveal.js Makefile
	pandoc -t revealjs -s \
	--slide-level 2 \
	-V theme=black \
	--highlight-style=zenburn \
	-V history=true \
	-V css=oofun.css \
	-V backgroundTransition=none \
	-V transitionSpeed=fast \
	oofun.org > $@

# oofun.pdf: oofun.org Makefile
# 	pandoc -t beamer -s \
# 	--slide-level 2 \
# 	--highlight-style=zenburn \
# 	-i oofun.org -o $@

oofun.pdf: oofun.org Makefile
	pandoc -t latex -i oofun.org -o $@

reveal.js:
	echo open https://github.com/hakimel/reveal.js/archive/3.3.0.tar.gz
	tar -xzf $(HOME)/Downloads/reveal.js-3.3.0.tar.gz
	mv reveal.js-3.3.0 reveal.js
