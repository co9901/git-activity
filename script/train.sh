#!/bin/bash
cd ..
mkdir -p bin

LIBS=bin
for f in `ls libs`; do LIBS=$LIBS:libs/$f; done

SRCS=
for f in `ls src`; do SRCS="$SRCS src/$f"; done

echo "Compiling$SRCS"
javac -cp $LIBS -d bin $SRCS

MAIN=Trainer

echo "Executing $MAIN.class"
java -cp $LIBS $MAIN

cd script