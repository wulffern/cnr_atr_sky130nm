
all:
	${foreach c, ${CELLS}, ${MAKE} run NAME=${c};}


include ../tech/make/sim.make

include ../cic/cells

LIB=CNR_ATR_SKY130NM
CELL=CNR_ATR
PREFIX=CNRATR_


post:
	${foreach c, ${CELLS}, cat header.md ${PREFIX}${c}/README.md > ../docs/_mos/${PREFIX}${c}.md;}

run:
	test -d ${PREFIX}${NAME} && cd ${PREFIX}${NAME} && make ${CORNER} OPT=${OPT}

gen:
	python3 gendirs.py
