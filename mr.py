import pylab as p
import numpy as np

# Defining the parameter
theta = 0.064; sigma = 0.27; alpha = 1;
n_path = 1000; n = n_partitions = 1000;
t = 1; R0 = 3;

# Creating brownian motion
dt = t/n; t = p.linspace(0,1,n+1)[:-1];
dB = p.randn(n_path,n+1)*p.sqrt(dt); dB[:,0] = 0;
B = dB.cumsum(axis=1);
 
# Generating R
R = p.zeros_like(B);
R[:,0] = R0
for col in range(n):
    R[:,col+1] = R[:,col]+alpha*(theta-R[:,col])*dt+[sigma*R[:,col]]*dB[:,col+1]
    
# Plotting
Rp = R[0:5:,:-1]
p.plot(t,Rp.transpose())
label = 'Time,$t$'; p.xlabel(label)
label = 'R(t)'; p.ylabel(label)
p.title('Realizations of Mean Reversal Process')
p.show()

#Calculating the expectation value of R(1)
R_1 = p.array(R[:,-1])
E_R_1 = np.mean(R_1)
print('E(R1) = ' + str(E_R_1))

#Calculating P[R(1)>2]
P = sum(R_1>2)/1000
print(' P[R(1)>2] = ' +str(P))
