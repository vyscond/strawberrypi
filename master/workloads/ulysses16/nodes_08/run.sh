for  i in {1..3}
do
    for j in {1..10}
    do
        echo "[serie][$i][$j][bgn]"
    
        python2 test.py $i $j ../strawberry_nodes.orbit &>> log.txt
    
        echo "[serie][$i][$j][bgn]"
    done 

done
