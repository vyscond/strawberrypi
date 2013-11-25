    for j in {1..10}
    do
        echo "[serie][3][$j][bgn]"
    
        python2 test.py 3 $j ../strawberry_nodes.orbit &>> log.txt
    
        echo "[serie][3][$j][bgn]"
    done 
