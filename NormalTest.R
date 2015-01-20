source('Input.R')
mainfolder <- "/home/xihao/R/Deng_Keller"
macro0 <- as.matrix(read.table("macro.txt"))
co20 <- as.matrix(read.table("co2.txt"))    

args <- commandArgs(TRUE)

filename <- args[1]

mle0 <- as.matrix(read.table(paste('Result1/Posterior/m', filename, '.dat', sep='')))

if (filename == 'Pop') {
xd <- c(t0, tm)
xs <- xd[7:Nm0]
d <- dPop
mle <- mle0[1:Nm0]
resi <- d[7:Nm0] - mle[7:Nm0]
scale <- log(d[7:Nm0]) - log(mle[7:Nm0])
incre <- scale[2:(Nm0-6)] - scale[1:(Nm0-7)]
mtitle <- 'Population'
yrl <- 'Billion'
sub <- 'Population'
} else if (filename == 'GDP') {
xd <- c(t0, tm)
xs <- xd[7:Nm0]
d <- dGDP
mle <- mle0[1:Nm0]
resi <- d[7:Nm0] - mle[7:Nm0]
scale <- log(d[7:Nm0]) - log(mle[7:Nm0])
incre <- scale[2:(Nm0-6)] - scale[1:(Nm0-7)]
mtitle <- 'Gross World Product'
yrl <- 'Trillion $/year'
sub <- 'GWP'
} else {
xd <- t
xs <- t[3:NC0]
d <- dCO2
mle <- mle0[1:NC0]
resi <- d[3:NC0] - mle[3:NC0]
scale <- log(d[3:NC0]) - log(mle[3:NC0])
incre <- scale[2:(NC0-2)] - scale[1:(NC0-3)]
mtitle <- 'Carbon Emission'
yrl <- 'Gt C/year'
sub <- 'Carbon'
}


figname <- paste('Figures/Norm', filename, '.pdf', sep='')

pdf(figname)

par(mfrow=c(3,2), pin=c(3.5, 2.7), mar=c(5,4.6,4,1.5))

plot(xd, d, type='p', pch=19, main=mtitle, 
     cex.axis=1.5, cex.main=1.5, cex.lab=1.5, font.lab=2,
     xlab='Year', ylab=yrl)

lines(xd, mle, lty=1, col='red', lwd=1.5)

legend('topleft', pch=c(19, NA), lty=c(NA, 1), lwd=c(1, 1.5), 
       col=c('black', 'red'), c('observations', 'best-fit'), 
       box.lwd=2, cex=1.3)

box(lwd=2)

plot(density(incre), main=paste('AR Error of Log', sub, sep=' '), 
     cex.axis=1.5, cex.main=1.5, cex.lab=1.5, font.lab=2, lwd=1.5,
     xlab='AR Error', ylab='pdf')

box(lwd=2)

plot(xs, resi, type='p', pch=19, main = 'Residuals', 
     cex.axis=1.5, cex.main=1.5, cex.lab=1.5, font.lab=2,
     xlab='Year', ylab=yrl)

box(lwd=2)

plot(ecdf(incre), main='', 
     cex.axis=1.5, cex.main=1.5, cex.lab=1.5, font.lab=2, lwd=1.5,
     xlab='AR Error', ylab='empirical cdf')

box(lwd=2)

plot(xs, c(0,incre), type='p', pch=19, 
     main = paste('AR Error of Log', sub, sep=' '), 
     cex.axis=1.5, cex.main=1.5, cex.lab=1.5, font.lab=2,
     xlab='Year', ylab='AR Error')

box(lwd=2)

std <- sqrt(mean(incre^2))
z <- incre/std

qqnorm(z, main='Q-Q Plot of AR Error', type='p', pch=19, axes=FALSE,
       cex.axis=1.5, cex.main=1.5, cex.lab=1.5, font.lab=2, 
       xlim=c(-3, 3), ylim=c(-3, 3),
       xlab='Normal theoretical quantiles', ylab='Actual quantiles')

il <- signif(std, 1)
plabels <- il * c(-3, NA, NA, 0, NA, NA, 3)

axis(side=1, at=seq(-3, 3, by=1), labels=plabels, cex.axis=1.5)
axis(side=2, at=seq(-3, 3, by=1), labels=plabels, cex.axis=1.5)
axis(side=4, at=seq(-3, 3, by=1), labels=FALSE)

abline(0, 1, lty=1, lwd=1.3, col='red')

legend('topleft', lty=1, lwd=1.5, 
       col='red', 'reference line', 
       box.lwd=2, cex=1.2)

box(lwd=2)


dev.off()
