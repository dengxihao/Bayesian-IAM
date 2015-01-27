## plot marginal posterior probability density of forecasts at 2050, 2100 and 2150

source('Input.R')

args <- commandArgs(TRUE)

filename <- args[1]

a1 <- paste("Result1/Posterior/Pr", filename, ".dat", sep="")

pdf1 <- as.matrix(read.table(a1))

if (filename == 'Pop') {
label <- paste("Population", "\n(Billion)", sep=" ")
xmax <- 14.0
} else if (filename == 'GDP') {
label <- paste("GWP", "\n(Trillion $/year)", sep=" ")
xmax <- 600.0
} else {
label <- paste("Carbon", "\n(Gt C/year)", sep=" ")
xmax <- 90.0
}

figname <- paste("Figures/P",
                 args[1], ".pdf", sep="")

pdf(figname)

par(pin=c(3.5, 2.7), mar=c(9,5,3,4), mgp=c(7.5,2,0))

xpdf1 <- density(pdf1[,1][pdf1[,1] < xmax])$x
ypdf1 <- density(pdf1[,1][pdf1[,1] < xmax])$y

xpdf2 <- density(pdf1[,2][pdf1[,2] < xmax])$x
ypdf2 <- density(pdf1[,2][pdf1[,2] < xmax])$y

xpdf3 <- density(pdf1[,3][pdf1[,3] < xmax])$x
ypdf3 <- density(pdf1[,3][pdf1[,3] < xmax])$y


######

ylo <- 0
yup <- 1.05*max(max(ypdf1), max(ypdf2), max(ypdf3))

# plot density of forecast at 2050
plot(xpdf1,ypdf1, type='l', col='blue', main="", xlab=label, ylab="", 
         ylim=c(ylo, yup), xlim=c(6, xmax), xaxt='n',
         cex.axis=2.5, cex.lab=2.5, font.lab=2, 
         lwd=5, lty=1)

# define axes
if (filename == 'Pop'){
xlabels <- c(6, 8, 10, 12, 14)
axis(side=1, at=seq(6, 14, by=2), labels=xlabels, cex.axis=2.5)
} else if (filename == 'GDP'){
xlabels <- c(0, 150, 300, 450, 600)
axis(side=1, at=seq(0, 600, by=150), labels=xlabels, cex.axis=2.5)
} else {
xlabels <- c(0, 30, 60, 90)
axis(side=1, at=seq(0, 90, by=30), labels=xlabels, cex.axis=2.5)
}

# plot density of forecast at 2100
lines(xpdf2, ypdf2, col='red', lwd=5, lty=1)

# plot density of forecast at 2150
lines(xpdf3, ypdf3, col='green', lwd=5, lty=1)

legend('topright', lty=c(1, 1, 1), lwd=c(2.6, 2.6, 2.6), 
       col=c('blue', 'red', 'green'), 
       c('2050', '2100', '2150'), 
       box.lwd=2, cex=1.6)

box(lwd=4) 

dev.off()

