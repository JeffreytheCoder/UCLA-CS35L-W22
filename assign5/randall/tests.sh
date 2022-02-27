#!/bin/sh

nBytes=100

if [ "$(./randall "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i rdrand "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i rdrand "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i mrand48_r "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i mrand48_r "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i /dev/random "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i /dev/random "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i /dev/random "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i /dev/random "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -o stdio "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -o stdio "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -o 0 "$nBytes" | wc -c)" = 0 ]
then
    :
else
    echo "Failed: ./randall -o 0 "$nBytes" | wc -c"
    exit 1
fi


if [ "$(./randall -o 50 "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -o 50 "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -o 69 "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -o 69 "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -o "$nBytes" "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -o "$nBytes" "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -o 333 "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -o 333 "$nBytes" | wc -c"
    exit 1
fi

if [ !$(./randall -i 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -i"
    exit 1
fi

if [ !$(./randall -o 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -o"
    exit 1
fi

if [ !$(./randall -i rdrand 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -i rdrand"
    exit 1
fi

if [ !$(./randall -i mrand48_r 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -i mrand48_r"
    exit 1
fi

if [ !$(./randall -i /dev/random 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -i /dev/random"
    exit 1
fi

if [ !$(./randall -i hello 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -i hello"
    exit 1
fi

if [ !$(./randall -i hello "$nBytes" 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -i hello "$nBytes""
    exit 1
fi

if [ !$(./randall -o stdio 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -o stdio"
    exit 1
fi

if [ !$(./randall -o 5 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -o 5"
    exit 1
fi

if [ !$(./randall -o hello "$nBytes" 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -o hello "$nBytes""
    exit 1
fi

if [ !$(./randall -o -10 "$nBytes" 2> /dev/null) ]
then
    :
else
    echo "Failed: ./randall -o -10 "$nBytes""
    exit 1
fi

if [ "$(./randall -i mrand48_r -o stdio "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i mrand48_r -o stdio "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i mrand48_r -o 5 "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i mrand48_r -o 5 "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i rdrand -o stdio "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i rdrand -o stdio "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i rdrand -o 5 "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i rdrand -o 5 "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i /dev/random -o stdio "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i /dev/random -o stdio "$nBytes" | wc -c"
    exit 1
fi


if [ "$(./randall -i /dev/random -o 5 "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i /dev/random -o 5 "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i /dev/urandom "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i /dev/urandom "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i /dev/urandom -o stdio "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i /dev/urandom -o stdio "$nBytes" | wc -c"
    exit 1
fi

if [ "$(./randall -i /dev/urandom -o 5 "$nBytes" | wc -c)" = "$nBytes" ]
then
    :
else
    echo "Failed: ./randall -i /dev/urandom -o 5 "$nBytes" | wc -c"
    exit 1
fi

echo "Passed all tests"
