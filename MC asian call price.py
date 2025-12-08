from numpy.random import randint as flip 
from numpy import exp, sqrt, log, mean,std
import matplotlib.pyplot as plt

def StockPricePath(S, sigma, r, T, N):
    Path=[S]
    h=T/N
    W=2*flip(2,size=N)-1
    for i in range(N):
        Path.append(S*exp((r-sigma**2/2)*h*(i+1)+sigma*sqrt(h)*sum(W[:i+1])))
    return Path

plt.plot(log(StockPricePath(100,0.05,0.05,1/2,100)))

def AsianCallPrice(Path, K):
    return max((mean(Path)-K),0)
def AsianPutPrice(Path, K):
    return max((K-mean(Path)),0)
AsianPutPrice(StockPricePath(100,0.5,0.05,1/2,100), 100)

def MonteCarloAsianCall(S, sigma, r, T,K, N,n):
    Payoff=[]
    for _ in range(n):
        Payoff.append(AsianCallPrice(StockPricePath(S, sigma, r, T, N),K))
    return[exp(-r*T)*mean(Payoff), 1.96*std(Payoff)/sqrt(n)]

print(MonteCarloAsianCall(100,0.5,0.05,1/2,100, 100, 10000))