
from traceback import format_exc , print_exc
from vyky      import GeneticAlgorithm

import os

def run( arg ):
    
    print os.path.abspath('.')
        
    try :
        
        ret = GeneticAlgorithm( arg.generations , arg.population_length , arg.mutation_rate , 'tsplib/'+arg.tsp_instance ).run()
                
        return [ ret , '' ] 

    except :
        
        print_exc()
        
        return [ '' , format_exc() ]
