from gurobipy import *
import math

rest=10
############################################################################################################################
def gupta_et_al(k, alpha):
    s=0; t=0
    for i in range(k):
        s += 1/(i+1); 
        t += 1/(i+1); t -= math.log(i+1)/(8*(i+1)*k)
    s -= 1/(8*k)
    return min(s,t)
############################################################################################################################
def splittable_bompadre_et_al(k, alpha):
    A=2*k*k-2*k; B=2-alpha+alpha/k-2/(k+1)+2*k*k-2*k; C=1-alpha+alpha/k-2/(k+1); root=(-B+math.sqrt(B*B-4*A*C))/(2*A)
    return 2-2/(k+1)+2*root*(1-1/k)*k*k
############################################################################################################################
def unsplittable_bompadre_et_al(k, alpha):
    if k%2==1: 
        return unsplittable_bompadre_et_al(2*k, alpha)
    AA=3-2/k-1/(k+1)+2/(k*(k+1)); BB=2*(1-1/k)*k*k; CC=2+(1-2/k)*alpha; A=BB; B=AA+BB-CC+2; C=AA-CC
    root=(-B+math.sqrt(B*B-4*A*C))/(2*A)
    return AA+BB*root
############################################################################################################################        
def splittable_blauth_et_al(k, alpha):
    return alpha+1-1.005/3000-alpha/k

def unsplittable_friggstad_et_al(k, alpha):
    if k%2==1: 
        return unsplittable_friggstad_et_al(2*k, alpha)
    return alpha+1+math.log(2)+math.log(1-1.005/3000)-2*alpha/k
############################################################################################################################
def splittable_initial_zhao_xiao(k, alpha):
    if k>=3 and 1<=alpha and alpha<=7/6: return alpha+1-alpha/k-(alpha-1/2)/k
    elif 3<=k and k<=5 and 7/6<=alpha and alpha<=3/2: return (13*k-11)/(6*k)
    elif 6<=k and 7/6<=alpha and alpha <=3/2: return alpha+1-alpha/k-4*(alpha-1)/k
    
def splittable_further_zhao_xiao(k, alpha):
    l=math.ceil( (math.sqrt(2*k-1)-1)/2 )
    return 2.5-(2*l*l+k+l-1)/(2*k*l)
    
def unsplittable_initial_zhao_xiao(k, alpha):
    fk = math.floor(k/2)
    if k>=3 and k<=5: return (2*fk+1)/(fk+1)+math.log(k/(fk+1))
    elif k==6 and 7/6<=alpha and alpha <=3/2: return 15/8+math.log(4/3)
    elif k==7 and 17/12<=alpha and alpha <=3/2: return 33/16+math.log(4/3)
    else: return ((alpha+1)*fk+1)/(fk+1) + math.log((k-4*(alpha-1))/(fk+1))
    
def unsplittable_further_zhao_xiao(k, alpha):
    fk = math.floor(k/2)
    C = fk/(fk+1)*1/2
    if math.floor((-(C+1)+math.sqrt((C+1)*(C+1)+4*k*C))/2) < math.floor((-(C+1)+math.sqrt((C+1)*(C+1)+4*(k+1)*C))/2):
        zstar = math.floor((-(C+1)+math.sqrt((C+1)*(C+1)+4*(k+1)*C))/2)
        xstar = 1/C - (k-2*zstar)/(zstar*zstar+zstar)
        return 1+math.log((k-2*math.floor(1/xstar)+math.floor(1/xstar)*math.floor(1/xstar)*xstar+math.floor(1/xstar)*xstar)/(fk+1)) + fk/(fk+1)*(3-xstar)/2
    else:
        z0 = (math.sqrt(fk*fk+8*fk*(fk+1)*(k+1))-fk)/(4*(fk+1))
        return max(g(k,math.ceil(z0)), g(k,math.floor(z0)))
    
def g(k, z):
    if z == 0: return -1
    fk = math.floor(k/2)
    return 1+math.log((k-z+1)/(fk+1))+fk/(fk+1)*(3-1/z)/2
############################################################################################################################        
alpha=3/2
############################################################################################################################       
print('SPLITTABLE')
print(f"{'k':<3} {'Gupta et al.':<15} {'Bompadre et al.':<18} {'Blauth et al.':<18} {'Initial Zhao & Xiao':<22} {'Further Zhao & Xiao':<22}")
for i in range(8):
    k = 3 + i
    x1 = round(gupta_et_al(k, alpha), rest)
    x2 = round(splittable_bompadre_et_al(k, alpha), rest)
    x3 = round(splittable_blauth_et_al(k, alpha), rest)
    x4 = round(splittable_initial_zhao_xiao(k, alpha), rest)
    x5 = round(splittable_further_zhao_xiao(k, alpha), rest)
    print(f"{k:<3} {x1:<15} {x2:<18} {x3:<18} {x4:<22} {x5:<22}")
############################################################################################################################       
print('UNSPLITTABLE')
print(f"{'k':<3} {'Gupta et al.':<15} {'Bompadre et al.':<18} {'Friggstad et al.':<18} {'Initial Zhao & Xiao':<22} {'Further Zhao & Xiao':<22}")
for i in range(8):
    k = 3 + i
    x1 = round(gupta_et_al(k, alpha), rest)
    x2 = round(unsplittable_bompadre_et_al(k, alpha), rest)
    x3 = round(unsplittable_friggstad_et_al(k, alpha), rest)
    x4 = round(unsplittable_initial_zhao_xiao(k, alpha), rest)
    x5 = round(unsplittable_further_zhao_xiao(k, alpha), rest)
    print(f"{k:<3} {x1:<15} {x2:<18} {x3:<18} {x4:<22} {x5:<22}")

