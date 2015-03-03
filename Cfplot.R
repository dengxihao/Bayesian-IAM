## plot percentiles of hindcasts and forecasts of carbon emission

suppressPackageStartupMessages(library("grid"));
suppressPackageStartupMessages(library("methods"));
suppressPackageStartupMessages(library("spam"));
suppressPackageStartupMessages(library("maps"));
suppressPackageStartupMessages(library("fields"));

###############################################################################

source('Input.R')

foldname <- 'Result1/Posterior/'

# load percentiles of hindcasts and forecasts of carbon emission
P <- as.matrix(read.table(paste(foldname, 'PCO2.dat', sep='')))

# load DICE, FUND and RCP model scenarios
dice <- as.matrix(read.table('dice_bau_2150.csv', sep=',', skip=1))

fund <- as.matrix(read.table('fund.dat'), sep=' ')
tfund <- 1951:3000

rcplabel <- read.table('RCP.dat', sep=' ', nrow=1)
rcp <- as.matrix((read.table('RCP.dat', sep=' ', skip=1)))
trcp <- rcp[,1]

pdf('Figures/Cfore.pdf')

par(mfrow=c(2, 1), pin=c(3.5, 2.7), mar=c(5,4.6,4,1.5))

x <- c(t0, t1)

#####################################################################################
xlabels <- c(1700, NA, NA, 1850, NA, NA, 2000, NA, NA, 2150)

pcolor <- colorRampPalette(c('red', 'orange', 'yellow', 'green', 'blue'))(196)

plot(x, type='l', main='Carbon Emission', axes=FALSE, 
     xlab='Year', ylab='Gt C/year',
     xlim=c(1700, 2150), ylim=c(0,80),
     cex.axis=1.5, cex.lab=1.3, cex.main=1.5, font.lab=2, font.main=2,
     lty=1, lwd=0.5, col='white')

# polygon plot
for (i in 1:196) {

polygon(c(x, rev(x)), c(P[3,], rev(P[199-i,])), 
        col=pcolor[i], border=pcolor[i])

}

plabels <- c(0, NA, 40, NA, 80)

axis(side=1, at=seq(1700, 2150, by=50), labels=xlabels, cex.axis=1.5, pos=-3, lwd=2.3)
axis(side=2, at=seq(0, 80, by=20), labels=plabels, cex.axis=1.5, pos=1700, lwd=2.3)
axis(side=3, at=seq(1700, 2150, by=50), tck=0, labels=FALSE, pos=80, lwd=2.3)
axis(side=4, at=seq(0, 80, by=20), labels=FALSE, pos=2150, lwd=2.3)

points(t, dCO2, type='p', pch=19, 
      cex=0.8)

lines(dice[,1], 3/11*dice[,4], lwd=3, lty=2, col='black')

lines(tfund[1:200], fund[1:200,3], lwd=3, lty=4, col='black')

lines(trcp[1:386], rcp[1:386,2], lwd=3, lty=3, col='black')

lines(trcp[1:386], rcp[1:386,3], lwd=3, lty=3, col='black')

lines(trcp[1:386], rcp[1:386,4], lwd=3, lty=3, col='black')

lines(trcp[1:386], rcp[1:386,5], lwd=3, lty=3, col='black')

lines(trcp[1:386], rcp[1:386,6], lwd=3, lty=3, col='black')

lines(trcp[1:386], rcp[1:386,7], lwd=3, lty=3, col='black')

legend(1875, 80, pch=c(19, NA, NA, NA), lty=c(NA, 2, 4, 3), 
       lwd=c(2, 2, 2, 2), col=c('black', 'black', 'black', 'black'),        
       c('observations', 'DICE', 'FUND', 'RCP'), 
       box.lwd=1.7, cex=0.8)

lines(c(t[NC0], t[NC0]), c(-3, 80), lty=5, lwd=2.5, col='grey')
lines(c(1700, 1700), c(0, -3), lwd=2.3)
lines(c(2150, 2150), c(0, -3), lwd=2.3)

my_breaks <- c('10%', '30%', '50%', '70%', '90% percentile')

image.plot(legend.only=TRUE, zlim=0.01*range(1,99), col=rev(pcolor), 
           smallplot=c(0.19,0.22, 0.33,0.74), 
           axis.args = list(at = seq(0.1, 0.9, 0.2), labels=my_breaks))

#################################################################################
xlabels1 <- c(1950, 1975, 2000, 2025, 2050)

plot(x, type='l', main='Carbon Emission (Detail)', axes=FALSE, 
     xlab='Year', ylab='Gt C/year',
     xlim=c(1950, 2050), ylim=c(0,40),
     cex.axis=1.5, cex.lab=1.3, cex.main=1.5, font.lab=2, font.main=2,
     lty=1, lwd=0.5, col='white')

for (i in 1:196) {

polygon(c(x[201:301], rev(x[201:301])), 
        c(P[3, 201:301], rev(P[199-i, 201:301])), 
        col=pcolor[i], border=pcolor[i])

}

plabels1 <- c(0, NA, 20, NA, 40)

axis(side=1, at=seq(1950, 2050, by=25), labels=xlabels1, cex.axis=1.5, pos=0, lwd=2.3)
axis(side=2, at=seq(0, 40, by=10), labels=plabels1, cex.axis=1.5, pos=1950, lwd=2.3)
axis(side=3, at=seq(1950, 2050, by=25), tck=0, labels=FALSE, pos=40, lwd=2.3)
axis(side=4, at=seq(0, 40, by=10), labels=FALSE, pos=2050, lwd=2.3)

points(t[200:300], dCO2[200:300], type='p', pch=19, cex=0.8)

lines(dice[1:9,1], 3/11*dice[1:9,4], lwd=3, lty=2, col='black')

lines(tfund[1:100], fund[1:100,3], lwd=3, lty=4, col='black')

lines(trcp[185:286], rcp[185:286,2], lwd=3, lty=3, col='black')

lines(trcp[185:286], rcp[185:286,3], lwd=3, lty=3, col='black')

lines(trcp[185:286], rcp[185:286,4], lwd=3, lty=3, col='black')

lines(trcp[185:286], rcp[185:286,5], lwd=3, lty=3, col='black')

lines(trcp[185:286], rcp[185:286,6], lwd=3, lty=3, col='black')

lines(trcp[185:286], rcp[185:286,7], lwd=3, lty=3, col='black')

legend(1984, 40, pch=c(19, NA, NA, NA), lty=c(NA, 2, 4, 3), 
       lwd=c(2, 2, 2, 2), col=c('black', 'black', 'black', 'black'),        
       c('observations', 'DICE', 'FUND', 'RCP'), 
       box.lwd=1.7, cex=0.78)

lines(c(t[NC0], t[NC0]), c(0, 40), lty=5, lwd=2.5, col='grey')

my_breaks <- c('10%', '30%', '50%', '70%', '90% percentile')

image.plot(legend.only=TRUE, zlim=0.01*range(1,99), col=rev(pcolor), 
           smallplot=c(0.19,0.22, 0.37,0.74), 
           axis.args = list(at = seq(0.1, 0.9, 0.2), labels=my_breaks))

#################################################################################

dev.off()
