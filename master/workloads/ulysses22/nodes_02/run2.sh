    for j in {7..10}
    do
        echo "[serie][1][$j][bgn]"
    
        python2 test.py 1 $j ../strawberry_nodes.orbit &>> log.txt
    
        echo "[serie][1][$j][bgn]"
    done 

