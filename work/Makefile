
#- Core makefile provides the following commands:
# -----------------------------------------------------------
# ip: generate ../design/<LIB> from ../cic/ip.json
# gds: generate gds/<CELL>.gds
# cdl: generate cdl/<CELL>.cdl
# lvs: Check cdl/<CELL>.cdl versus ../design/<LIB>/<CELL>.mag
# lpe: Extract parasitics lpe/<CELL>.spi
# drc: Run design rule checks on ../design/<LIB>/<CELL>.mag
# -----------------------------------------------------------



PREFIX=CNRATR_
LIB=CNR_ATR_SKY130NM
CELL=CNR_ATR

#- Provide cells you want to check for the lvsall drcall commands
-include ../cic/cells

include ../tech/make/core.make
