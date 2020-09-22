# Random Circuit 1 qiskit statevector
# amount of qubits we are going to run
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, IBMQ
from qulacs import Observable, QuantumState, QuantumCircuit as QC
import time
import tracemalloc
import resource
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import mark_inset, inset_axes
from qiskit.visualization import plot_histogram
import numpy as np
import random

depth = 20
width = 20

qisRC1t = np.array([], dtype=float)
qisRC1m = np.array([], dtype=float)

# array with every possible gate for this implementation 
arr = ['T', 'X(1/2)', 'Y(1/2)']

qubitsArrayCZ_prev = width*[False]
qubitsArrayT_prev = width*[False]
qubitsArrayX_prev = width*[False]
qubitsArrayY_prev = width*[False]

qubitsArrayCZ = width*[False]
qubitsArrayT = width*[False]
qubitsArrayX = width*[False]
qubitsArrayY = width*[False]

# initializing variable
CZGate = True
CZ = width/2.0
counter = 0 
times = 10

#ratio_tot = 0.0
ratio_avg = 0.0

for w in range(2, width):
    print ("width {}".format(w))
    tt_tot = 0.0
    rss_tot = 0.0
    ratio_tot = 0.0
    # Randomly applying the random circuit gate set
    for t in range(0, times):
        CZ_tot = 0.0
        T_tot = 0.0
        X_tot = 0.0
        Y_tot = 0.0
        single_tot = 0.0
        
        tracemalloc.start()  
        t_start = time.perf_counter()
    
        # defining the device 
        q = QuantumRegister(w, 'q')
        c = ClassicalRegister(w, 'c')
        circR1 = QuantumCircuit(q, c)
    
        # apply cycle Hadamards
        circR1.h(q)
    
        for i in range(0, depth):
            if w < 4:
                initCZgates = int(w/2.0)
            else:
                initCZgates = int((w)/4.0) # decide on this one
            # apply CZ randomly
            for j in range(0, initCZgates):
                while CZGate:
                    q0 = random.randint(0, w - 2 )
                    q1 = q0 + 1
                    if i == 0:
                        if qubitsArrayCZ[q0] == False and qubitsArrayCZ[q1] == False:
                            circR1.cz(q0,q1)
                            qubitsArrayCZ[q0] = True
                            qubitsArrayCZ[q1] = True
                            CZGate = False
                    elif i != 0 and qubitsArrayCZ_prev[q0] == False:
                        if qubitsArrayCZ[q0] == False and qubitsArrayCZ[q1] == False:
                            circR1.cz(q0,q1)
                        
                            qubitsArrayCZ[q0] = True
                            qubitsArrayCZ[q1] = True
                            CZGate = False
                    else:
                        counter += 1
                    if counter > 2:
                        break
                counter = 0 
                        
                CZGate = True
        
            # apply single gate at random in rest qubits if previous gate is CZ:
            for q in range(0, w):   
           
                if qubitsArrayCZ[q] == False:
                    if i == 0:
                        while True:
                            rGate = np.random.choice(arr)
                            if rGate == 'T' and qubitsArrayT_prev[q] == False:
                                circR1.t(q)
                                qubitsArrayT[q] = True 
                                break
                            elif rGate == 'X(1/2)' and qubitsArrayX_prev[q] == False:
                                circR1.x(q)
                                qubitsArrayX[q] = True
                                break
                            elif rGate == 'Y(1/2)' and qubitsArrayY_prev[q] == False:
                                circR1.y(q)
                                qubitsArrayY[q] = True
                                break
                            else:
                                counter = counter + 1
                            if counter > 10:
                                break

                    elif i != 0 and qubitsArrayCZ_prev[q] == True:
                        while True:
                            rGate = np.random.choice(arr)
                            if rGate == 'T' and qubitsArrayT_prev[q] == False:
                                circR1.t(q)
                                qubitsArrayT[q] = True 
                                break
                            elif rGate == 'X(1/2)' and qubitsArrayX_prev[q] == False:
                                circR1.x(q)
                                qubitsArrayX[q] = True
                                break
                            elif rGate == 'Y(1/2)' and qubitsArrayY_prev[q] == False:
                                circR1.y(q)
                                qubitsArrayY[q] = True
                                break
                            else:
                                counter += 1
                            if counter > 10:
                                break
                    counter = 0
            # compute ratio control and single gates
            CZ = qubitsArrayCZ.count(True)
            T = qubitsArrayT.count(True)
            X = qubitsArrayX.count(True)
            Y = qubitsArrayY.count(True)
            
            single = T + Y + X
            CZ_tot += CZ
            T_tot += T
            Y_tot += Y
            X_tot += X
            single_tot += single
            qubitsArrayT_prev = qubitsArrayT
            qubitsArrayX_prev = qubitsArrayX
            qubitsArrayY_prev = qubitsArrayY
            qubitsArrayCZ_prev = qubitsArrayCZ
            qubitsArrayT = [ False for x in range(width)]
            qubitsArrayX = [ False for x in range(width)]
            qubitsArrayY = [ False for x in range(width)]
            qubitsArrayCZ = [ False for x in range(width)]
            # compute ratio control and single gates

        # the default backend
        backend = Aer.get_backend('statevector_simulator')
        state = execute(circR1, backend).result().get_statevector()

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics('lineno')
        tracemalloc.stop()
        max_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rss_tot += max_rss

        t_stop = time.perf_counter()
        t_tot = t_stop - t_start

        tt_tot += t_tot

        if t < times - 1:
            del q
            del c
            del circR1
            del state        


        #print (" Time {}".format(t))
        #print ("Ratio single/controlled: {}".format(single_tot/(CZ_tot/2.0)))
        #print (" T gates: {}".format(T_tot))
        #print (" X gates: {}".format(X_tot))
        #print (" Y gates: {}".format(Y_tot))
        #print (" CZ gates: {}".format(CZ_tot/2.0))
       # print (" Total  gates: {}".format(CZ_tot/2.0 + single_tot))
        #print ("time: {}".format(t_tot))
        ratio_tot += (single_tot/(CZ_tot/2.0))
    ratio_avg = ratio_tot/times
    ratio_tot = 0.0
    rss_avg = rss_tot / times 
    qisRC1m = np.append(qisRC1m, [rss_avg])
    t_avg = tt_tot / times
    qisRC1t = np.append(qisRC1t, [t_avg])
    #print ("time_av: {}".format(t_avg))
    print ("ratio_av: {}".format(ratio_avg))
print (qisRC1t)
print(qisRC1m)              
 
