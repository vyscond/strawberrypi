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

TSP_INSTANCE = "ulysses16.tsp"
GENERATIONS  = 50
POPULATION   = 16
TASKS        = 100
NODES        = [ 'war' , 'death' , 'pestilence' , 'famine' , 'envy' , 'lust' , 'wrath' , 'greed' ]


if len( sys.argv ) == 4 :

    tmp = []

    task_list = [ str(Task( app='gatsp' , argv={ "generations" : GENERATIONS , "population_length" : POPULATION  , "mutation_rate" : 1 , "tsp_instance" : TSP_INSTANCE } ) ) ] * TASKS 

    expedition_start = time.time()

    task_result_list = Planet( str( sys.argv[3] ) ).launch_expeditions( task_list , NODES )

    expedition_end = time.time()

    tmp.append( 'total expedition time                 : ' + str( expedition_end - expedition_start ) )
    tmp.append( 'total expedition time per task        : ' + str( ( expedition_end - expedition_start ) /len(task_result_list)) )

    average_task_execution_time = 0

    for i in xrange( len(task_result_list) ) :

        task = Task( json_str=task_result_list[ i ] )

        average_task_execution_time += task.execution_time

    tmp.append( 'total task exec time                  : ' + str(average_task_execution_time) )
    tmp.append( 'average task exec time per task       : ' + str(average_task_execution_time/len(task_result_list)) )
    tmp.append( 'average task exec time per node       : ' + str(average_task_execution_time/len(NODES)) )
    tmp.append( 'average task exec time per generation : ' + str(average_task_execution_time/(GENERATIONS*TASKS)) )

    output = open( sys.argv[0][:-3]+'_serie'+str(sys.argv[1])+'_exercise_'+str(sys.argv[2])+'.result' , 'w' )
    output.write( '\n'.join(tmp) )
    output.close()
