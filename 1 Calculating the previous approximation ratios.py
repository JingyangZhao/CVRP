import math
#t,r<=1/6
def zeta(rho, tau, epsilon):
    return (3*rho+tau-4*tau*rho)/(1-rho) + epsilon/(tau*rho)*(1-tau*rho-(3*rho+tau-4*tau*rho)/(1-rho))
############################################################################################################################################
def function(rho, tau, epsilon):
    theta = 1/(1+math.sqrt(3*epsilon/(2+zeta(rho,tau,epsilon))))
    if theta > 1-tau:
        theta = 1-tau
    return (1+zeta(rho,tau,epsilon))/theta + (1-tau-theta)/(theta*(1-tau)) + 3*epsilon/(1-theta) + 3*rho/(1-rho)/(1-tau) - 1
############################################################################################################################################
def f(epsilon):
    min_found=1000
    for i in range(1666):
        for j in range(1666):
            rho=(i+1)/10000; tau=(j+1)/10000
            tem = function(rho, tau, epsilon)
            if min_found > tem: min_found = tem
    return min_found
############################################################################################################################################
alpha=3/2
####################
#""" splittable
if 1:
    epsilon=1.005/3000-0.000000005 #1.005/3000-0.000000006------1.005/3000-0.000000005
    
    g=f(epsilon)
    print(2+g); print(alpha+1-epsilon)
    
    if alpha+1-epsilon < 2+g: print("epsilon should be smaller")
    else: print("epsilon can be bigger")
####################
### unsplittable
elif 0:
    epsilon=1.005/3000-0.000000005 #1.005/3000-0.000000006------1.005/3000-0.000000005
    
    g=f(epsilon)
    print(2+math.log(2)+g); print(alpha+1+math.log(2)+math.log(1-epsilon))
    
    if alpha+1+math.log(2)+math.log(1-epsilon) < 2+math.log(2)+g: print("epsilon should be smaller")
    else: print("epsilon can be bigger")