#!/bin/bash
LD_LIBRARY_PATH=~/usr/lib:/home/grad/samee1/packages/gsl-1.14/lib
export LD_LIBRARY_PATH
BASE=.
DATA=$BASE/data
SRC=$BASE/src
OUTFILE="ind_model.out"
PAR_DIR=$BASE/par
LOG=$BASE/log
OUT=$BASE/out

python pysrc/make_mean_input.py $DATA/factor_expr.tab $DATA/dperk.tab $DATA/expr.tab

$SRC/seq2expr -s $DATA/seqs_ind.fa -rs $DATA/r_seqs.fa -e $DATA/expr.tab -m $DATA/factors.wtmx -f $DATA/factor_expr.tab -o Direct -oo SSE -fo $OUT/ind.out -na 30 -i $DATA/factor_info.txt -p $PAR_DIR/ind.par -ct 25 -c $DATA/coop.txt -rt 250 -ff $DATA/free_fix.txt -ft $DATA/factor_thr.txt -dp $DATA/dperk.tab > $LOG/ind.log
