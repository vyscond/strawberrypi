#
# Owner
#    Ramon M. "Vyscond"
#
# email
#   vyscond@gmail.com
#
# github
#   vyscond
#
# twitter
#   @vyscond
#
#
# License 
#   This software is licensed under GNU General Public License, version 3 (GPL-3.0)

from cosmos import Task , Planet
import sys , time , json

# 0 test.py

# 1 tsplib instance
# 2 population
# 3 generations

# 4 serie
# 5 carga
# 6 tasks
# 7 node qtt

# 8 orbit file

# 9 output results

if len( sys.argv ) == 10 :
    
    # ------------------------------------------------------------------
    
    TSP_INSTANCE = sys.argv[1]
    POPULATION   = int(sys.argv[2])
    GENERATIONS  = int(sys.argv[3])
    TASKS        = int(sys.argv[6])
    NODES        = [ 'war' , 'death' , 'pestilence' , 'famine' , 'envy' , 'wrath' ]
    NODES_QTT    = int(sys.argv[7])
    
    # ------------------------------------------------------------------
    
    tmp = []

    task_list = [ str(Task( app='vyky' , argv={ "generations" : GENERATIONS , "population_length" : POPULATION  , "mutation_rate" : 1 , "tsp_instance" : TSP_INSTANCE } ) ) ] * TASKS 

    expedition_start = time.time()
    
    task_result_list = Planet( str( sys.argv[3] ) ).launch_expeditions( task_list , NODES[ : NODES_QTT ] )
    
    expedition_end = time.time()

    # ------------------------------------------------------------------

    tmp.append( 'total expedition time                 : ' + str( expedition_end - expedition_start ) )
    tmp.append( 'total expedition time per task        : ' + str( ( expedition_end - expedition_start ) /len(task_result_list)) )

    average_task_execution_time = 0

    for i in xrange( len(task_result_list) ) :

        task = Task( json_str=task_result_list[ i ] )

        average_task_execution_time += task.execution_time

    # ------------------------------------------------------------------

    tmp.append( 'total task exec time                  : ' + str(average_task_execution_time) )
    tmp.append( 'average task exec time per task       : ' + str(average_task_execution_time/len(task_result_list)) )
    tmp.append( 'average task exec time per node       : ' + str(average_task_execution_time/NODES_QTT) )
    tmp.append( 'average task exec time per generation : ' + str(average_task_execution_time/(GENERATIONS*TASKS)) )
    
    
    print 'saving results at' , str(sys.argv[9])
    
    output = open( str(sys.argv[9])+TSP_INSTANCE+'_node'+str(NODES_QTT)+'_serie'+str(sys.argv[4])+'_exercise'+str(sys.argv[5])+'.txt' , 'w' )
    
    output.write( '\n'.join(tmp) )
    
    output.close()
