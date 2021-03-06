## plot marginal posterior probability density from mcmc samples

source('Input.R')

args <- commandArgs(TRUE)

# folders to save the figures
folder <- args[1]
subfolder <- args[2]

# index of the parameters
column <- strtoi(args[3]) 

mycols <- rep("NULL", 25)
mycols[column] <- NA
filename <- paste("Result", folder, "/", subfolder, "/samps.dat", sep="")

xs <- as.matrix(read.table(filename, colClasses=mycols))

label  <-  c("population growth rate\n(1/yr)",                        # 1
             "half-saturation constant\n(trillion $/(yr capita)",     # 2
             "population carrying capacity\n(billion)",               # 3
             "rate of technological progress\n(1/yr)",                # 4   
             "saturation level of\ntotal factor productivity",        # 5
             "capital deprecation rate\n(1/yr)",                      # 6
             "saving rate",                                           # 7
             "elasticity of production\nwith respect to labor",       # 8
             "labor participation rate",                              # 9 
             "rate of technological penetration\n(1/yr)",             # 10
             "carbon intensity technology 2\n(kg/$)",                 # 11
             "carbon intensity technology 3\n(kg/$)",                 # 12
             "half-saturation of technology 2\n(yr)",                 # 13  
             "half-saturation of techology 3\n(yr)",                  # 14
             "half-saturation of techology 4\n(yr)",                  # 15 
             "population in 1700\n(billion)",                         # 16
             "initial total factor productivity",        # Model      # 17
             "population AR coefficient",                             # 18 
             "GWP AR coefficient",                                    # 19
             "carbon AR coefficient",                                 # 20
             "AR error of log population",                            # 21
             "AR error of log GWP",                                   # 22  
             "AR error of log carbon",                                # 23
             "error of non-annual population\n(billion)",             # 24
             "error of non-annual GWP\n(trillion $/yr)")              # 25

# index of parameters with Gaussian priors
indn <- c(3, 7, 8, 9, 16)

pdf(paste("Figures/par", args[3], ".pdf", sep=""))

par(pin=c(3.5, 2.7), mar=c(9,5,3,4), mgp=c(7.5,2,0))

ys <- density(xs)
xb <- c(parlb[column], parub[column])

x <- ys$x
y <- ys$y * dunif(x, min=xb[1], max=xb[2]) * (xb[2]-xb[1])

xl <- xb

# plot posterior probability density
plot(x,y,type='l', col='blue', main="", 
         xlim=xl, ylim=c(0, 1.05*max(y)),
         cex.axis=2.5, xlab="", ylab="",
         lwd=5, lty=1)

title(xlab=label[column], ylab="",  cex.lab=2.5, font.lab=2) 

if (column %in% indn){
xp <- seq(xb[1], xb[2], length=100)
yp <- dunif(xp, min=xb[1], max=xb[2]) * (xb[2]-xb[1]) *
      dnorm(xp, mean=mean(xb),sd=(xb[2]-xb[1])/4) * 100/95
} else if (column %in% c(24, 25)){
xp <- seq(xb[1], xb[2], length=100)
yp <- dunif(xp, min=xb[1], max=xb[2]) * (xb[2]-xb[1]) *
      xp^(-1.0) * (1/(log(xb[2]) - log(xb[1])))
} else {
xp <- seq(xb[1], xb[2], length=100)
yp <- dunif(xp, min=xb[1], max=xb[2])
}

xp <- c(xb[1], xp, xb[2])
yp <- c(0, yp, 0)

#xp <- c(xp, xb[2])
#yp <- c(yp, 0)

# plot prior probability density
lines(xp, yp, lty=2, lwd=5, col='red')

if (x[which.max(y)]>=mean(xb)){
  lpos <- 'topleft'
} else{
  lpos <- 'topright'
}

#legend(lpos, lty=c(1, 2), lwd=c(2.6, 3), col=c('blue', 'red'), 
#       c('Posterior', 'Prior'), box.lwd=2, cex=1.85)

box(lwd=4) 

dev.off()
