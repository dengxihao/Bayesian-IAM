## plot percentiles of hindcasts and forecasts of population and GWP

library("grid", lib.loc="R_packages/");
library("methods", lib.loc="R_packages/");
library("spam", lib.loc="R_packages/");
library("maps", lib.loc="R_packages/");
library("fields", lib.loc="R_packages/");

###############################################################################

source('Input.R')

foldname <- 'Result1/Posterior/'

# load percentiles of hindcasts and forecasts of population and GWP
Pp <- as.matrix(read.table(paste(foldname, 'PPop.dat', sep='')))
Pg <- as.matrix(read.table(paste(foldname, 'PGDP.dat', sep='')))

# load DICE and FUND model scenarios
dice <- as.matrix(read.table('dice_bau_2150.csv', sep=',', skip=1))
tdice <- dice[,1]
fund <- as.matrix(read.table('fund.dat', sep=' '))
tfund <- 1951:3000

rate1 <- fund[45, 2]/dGDP[52]            # International dollar over 1995 USD ratio
rate2 <- rate1 * dice[1, 3]/fund[60, 2]  # International dollar over 2005 USD ratio 

pdf('Figures/Mfore.pdf')

par(mfrow=c(2, 1), pin=c(3.5, 2.7), mar=c(5,4.6,4,1.5))

x <- c(t0, tM)

#####################################################################################
xlabels <- c(1700, NA, NA, 1850, NA, NA, 2000, NA, NA, 2150)

# set colors characterizing the percentiles
pcolor <- colorRampPalette(c('red', 'orange', 'yellow', 'green', 'blue'))(196)

plot(x, type='l', main='Population', axes=FALSE, 
     xlab='Year', ylab='Billion',
     xlim=c(1700, 2150), ylim=c(0,12),
     cex.axis=1.5, cex.lab=1.3, cex.main=1.5, font.lab=2, font.main=2,
     lty=1, lwd=0.5, col='white')

# polygon plot of population forecast percentiles
for (i in 1:196) {

polygon(c(x, rev(x)), c(Pp[3,], rev(Pp[199-i,])), 
        col=pcolor[i], border=pcolor[i])

}

# defining axes
plabels <- c(0, 4, 8, 12)

axis(side=1, at=seq(1700, 2150, by=50), labels=xlabels, cex.axis=1.5, pos=0, lwd=1.7)
axis(side=2, at=seq(0, 12, by=4), labels=plabels, cex.axis=1.5, pos=1700, lwd=1.7)
axis(side=3, at=seq(1700, 2150, by=50), tck=0, labels=FALSE, pos=12, lwd=1.7)
axis(side=4, at=seq(0, 12, by=4), labels=FALSE, pos=2150, lwd=1.7)

# plot population observations
points(c(t0, tm), dPop, type='p', pch=19, 
      cex=0.6)

# plot separation line between hindcast and forecast
lines(c(tm[Nm0-1], tm[Nm0-1]), c(0, 12), lty=5, lwd=2.5, col='grey')

# plot DICE scenario
lines(tdice, dice[, 2]/1000, lty=2, lwd=3, col='black')

# plot FUND scenario
lines(tfund[1:200], fund[1:200, 1], lty=4, lwd=3, col='black')

legend(1870, 12, pch=c(19, NA, NA), lty=c(NA, 2, 4), 
       lwd=c(2, 2, 2), col=c('black', 'black', 'black'),        
       c('observations', 'DICE', 'FUND'), 
       box.lwd=1.7, cex=0.8)

my_breaks <- c('10%', '30%', '50%', '70%', '90% percentile')

image.plot(legend.only=TRUE, zlim=0.01*range(1,99), col=rev(pcolor), 
           smallplot=c(0.19,0.22, 0.37,0.74), 
           axis.args = list(at = seq(0.1, 0.9, 0.2), labels=my_breaks))


#################################################################################

plot(x, type='l', main='Gross World Product', axes=FALSE, 
     xlab='Year', ylab='Trillion $/year',
     xlim=c(1700, 2150), ylim=c(0,600),
     cex.axis=1.5, cex.lab=1.3, cex.main=1.5, font.lab=2, font.main=2,
     lty=1, lwd=0.5, col='white')

# polygon plot of hindcasts and forecasts of GWP
for (i in 1:196) {

polygon(c(x, rev(x)), c(Pg[3,], rev(Pg[199-i,])), 
        col=pcolor[i], border=pcolor[i])

}

plabels <- c(0, NA, 300, NA, 600)

axis(side=1, at=seq(1700, 2150, by=50), labels=xlabels, cex.axis=1.5, pos=-10, lwd=1.7)
axis(side=2, at=seq(0, 600, by=150), labels=plabels, cex.axis=1.5, pos=1700, lwd=1.7)
axis(side=3, at=seq(1700, 2150, by=50), tck=0, labels=FALSE, pos=600, lwd=1.7)
axis(side=4, at=seq(0, 600, by=150), labels=FALSE, pos=2150, lwd=1.7)

# plot GWP observations
points(c(t0, tm), dGDP, type='p', pch=19, 
      cex=0.6)

# plot separation line between hindcast and forecast
lines(c(tm[Nm0-1], tm[Nm0-1]), c(-10, 600), lty=5, lwd=2.5, col='grey')

lines(c(2150, 2150), c(0, -10), lwd=1.7)

lines(tdice, dice[, 3]*rate2, lty=2, lwd=3, col='black')

lines(tfund[1:200], fund[1:200, 2]*rate1, lty=4, lwd=3, col='black')

legend(1870, 600, pch=c(19, NA, NA), lty=c(NA, 2, 4), 
       lwd=c(2, 2, 2), col=c('black', 'black', 'black'),        
       c('observations', 'DICE', 'FUND'), 
       box.lwd=1.7, cex=0.8)

image.plot(legend.only=TRUE, zlim=0.01*range(1,99), col=rev(pcolor), 
           smallplot=c(0.19,0.22, 0.32,0.74), 
           axis.args = list(at = seq(0.1, 0.9, 0.2), labels=my_breaks))

dev.off()
