rm(list=ls())
library(deSolve)

syst <- function(t, y, parameters)
{   #parms[1]=r, parms[2]=a, parms[3]=e, parms[4]=m parms[5]=K
  #x[1]=N, x[2]=P
  parameters <- c(r, a, e, m, K)
  dy1 <- r*y[1]*(1-y[1]/K)-a*y[1]*y[2] # Equation de N
  dy2 <- e*a*y[1]*y[2]-m*y[2] # Equation de P
  list(c(dy1,dy2))
}

time <- seq(0, 100, by=0.1)
init <- c(10, 2)
r <- 0.2
a <- 0.2
e <- 1
m <- 0.4
K <- 10
parms <- c(r, a, e, m, K)

solution <- lsoda(y = init, times = time, func = syst, parms = parms)
plot(solution[,1], solution[,2])
