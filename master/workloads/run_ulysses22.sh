
if [ "@#" -lt 1 ]; then
    
    echo 'at least one node pls!'
    exit
fi

echo '[begin the tests with '$1' nodes]'

mkdir test_results_ulysses22

for serie in {1..3}
do
    for carga in {1..10}
    do
        echo "[Executing][Serie][1][workload][$carga/10]"
        echo "call line : python2 test.py ulysses16 16 50 $serie $carga  100 $1 ../../strawberry.orbit &> /dev/null"
        python2 test.py ulysses22 16 50 $serie $carga  100 $1 ../../strawberry.orbit test_results_ulysses22 &> /dev/null
    
    done
done
