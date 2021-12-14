#!/bin/bash

success=1
test_expected() {
    for f in test-data/*.fa; do
        coords=$f-coordinates
        expected=$f-get-subseqs-expected
        args=`eval echo $1`
        if ! cmp -s <(./get-subseqs $args) $expected; then
            echo "./get-subseqs $args did not produce the expected output"
            diff <(./get-subseqs $args) $expected
            echo
            success=0
        fi
    done
}

echo "Providing coordinates in a file"
test_expected "\$f \$coords"

echo "Providing coordinates on stdin"
test_expected "\$f < \$coords"

echo "Providing coordinates as `-` (stdin)"
test_expected "\$f - < \$coords"

if (( success == 1 )); then
    echo "Success."
else
    exit 2
fi
