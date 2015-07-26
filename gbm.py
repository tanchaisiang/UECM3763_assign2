import pylab as p
import numpy as np

# Setup parameters
mu = 0.1; sigma = 0.26; S0 = 39;
n_path = 1000; n=n_partitions = 1000;

# Create Brownian piaths
t = p.linspace(0,3,n+1);
dB = p.randn(n_path,n+1)/p.sqrt(n); dB[:,0] = 0;
B = dB.cumsum(axis=1);

# Calculate stock prices
nu = mu-sigma*sigma/2.0
S = p.zeros_like(B); S[:,0] = S0
S[:,1:] = S0*p.exp(nu*t[1:]+sigma*B[:,1:])

# Plot 5 realizations of the GBM
St = S[0:5]
label = 'Time,$t$'; p.xlabel(label)
label = 'Stock price,$S$'; p.ylabel(label)
p.title('Realizations of Geometric Brownian Motion')
p.plot(t,St.transpose())
p.show()

# Calcluations of the expectation value and variance of S(3)
S_3 = p.array(S[:,-1])
E_S_3 = np.mean(S_3)
Var_S_3 = np.var(S_3)
print('E(S3) = ' + str (E_S_3))
print('Var(S3) = ' + str(Var_S_3))

# Calculations of P[S(3)>39] and E[S(3)|S(3)>39]
P = (sum(S_3 >39)/ len (S_3>39))
print('P[S(3)>39] = ' + str (P))
E = sum(S_3 * (S_3>39))/sum(S_3>39)
print('E[S(3)|S(3)>39] = ' + str (E))
