# This R module load all the inputs of data, initial parameters, parameter bounds, etc.
 
   macro0 <- as.matrix(read.table("macro.txt"))    # observations of population and GWP
    co20 <- as.matrix(read.table("co2.txt"))       # observations of carbon emission  
    
    Nm0 <- length(macro0[,1])              # length of population observations  
    NC0 <- length(co20[,1])                # length of carbon emission observations
    tm <- macro0[2:Nm0,1]                  # observation times of population after 1700
    t <- co20[,1]                          # observation times of carbon emission
    t0 <- macro0[1,1]                      # initial observation time of population
    
   # hindcast and forecast time range of population and GWP 
    tM <- c(tm, ((tm[Nm0-1]+1):2150))  
   
   # hindcast and forecast time range of carbon emission   
    t1 <- t[1]:2150 

    dPop = macro0[, 2]                      # observations of population 
    dGDP = macro0[, 3]                      # observations of GWP
    dCO2 = co20[,2]                         # observations of carbon emission

   # the indices of population observation times in carbon emission observation time vector
    ind = match(tm, t)
   
    par0 <- as.matrix(read.table("parm1.txt"));

   # parameter bounds  
    parlb <- c(0.0001,
              1.0, 
              6.9,
              0.0007,
              5.3,
              0.01,
              0.18,
              0.6,
              0.51,
              0.005,
              0,
              0,
              1700,
              1700,
              2010,
              0.3,
              0.0,    # Model
              0.85,
              0.85,
              0.85,
              0.00001,
              0.00001,
              0.00001, 
              0.00001, 
              0.00001)

    parub <- c(0.15, 
               100.0, 
               14.4, 
               0.0212,
               16.11, 
               0.14, 
               0.26, 
               0.8, 
               0.67, 
               0.2, 
               0.5, 
               0.5, 
               2100, 
               2100, 
               2500, 
               0.9,          
               3.0,     # Model 
               1.0,
               1.0,
               1.0,
               0.006,
               0.05,
               0.1, 
               0.6, 
               2.0) 

   parb <- matrix(c(parlb, parub), nrow=length(parlb), ncol=2)














