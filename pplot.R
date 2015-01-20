source('Input.R')

args <- commandArgs(TRUE)

filename <- args[1]

if (filename == 'Pop' || filename == 'GDP') {
Ncols = 207
} else {
Ncols = 401
}

mycols <- rep("NULL", Ncols)
column <- Ncols - 100
mycols[column] <- NA
a1 <- paste("Result1/Posterior/Pr", filename, ".dat", sep="")
a2 <- paste("Result2/Posterior/Pr", filename, ".dat", sep="")
b1 <- paste("Result1/Prior/f", filename, ".dat", sep="")
b2 <- paste("Result2/Prior/P", filename, ".dat", sep="")

if (filename == 'Pop') {
label <- paste("Population", "2050", "\n(Billion)", sep=" ")
xmax <- 15.0
} else if (filename == 'GDP') {
label <- paste("GWP", "2050", "\n(Trillion $/year)", sep=" ")
xmax <- 240.0
} else {
label <- paste("Carbon", "2050", "\n(Gt C/year)", sep=" ")
xmax <- 50.0
}

pdf1 <- as.matrix(read.table(a1))
pdf1 <- pdf1[,1][pdf1[,1]<xmax]
pdf2 <- as.matrix(read.table(a2))
pdf2 <- pdf2[,1][pdf2[,1]<xmax]
pr1 <- as.matrix(read.table(b1, colClasses=mycols))
pr1 <- pr1[,1][pr1[,1]<xmax]
pr2 <- as.matrix(read.table(b2))
pr2 <- pr2[,1][pr2[,1]<xmax]

figname <- paste("Figures/",
                 args[1], "2050", ".pdf", sep="")

pdf(figname)

par(pin=c(3.5, 2.7), mar=c(9,5,3,4), mgp=c(7.5,2,0))

xpdf1 <- density(pdf1)$x
ypdf1 <- density(pdf1)$y

xpr1 <- density(pr1)$x
ypr1 <- density(pr1)$y

xpdf2 <- density(pdf2)$x
ypdf2 <- density(pdf2)$y

xpr2 <- density(pr2)$x
ypr2 <- density(pr2)$y

######

xlo <- min(min(xpdf1), min(xpr1), min(xpdf2), min(xpr2)) 
xup <- max(max(xpdf1), max(xpr1), max(xpdf2), max(xpr2)) 

ylo <- 0
yup <- 1.05*max(max(ypdf1), max(ypr1), max(ypdf2), max(ypr2))

plot(xpdf1,ypdf1, type='l', col='blue', main="", xlab=label, ylab="", 
         ylim=c(ylo, yup), xlim=c(0, xmax), xaxt='n',
         cex.axis=2.5, cex.lab=2.5, font.lab=2, 
         lwd=5, lty=1)

if (filename == 'Pop'){
xlabels <- c(0, 3, 6, 9, 12, 15)
axis(side=1, at=seq(0, 15, by=3), labels=xlabels, cex.axis=2.5)
} else if (filename == 'GDP'){
xlabels <- c(0, 60, 120, 180, 240)
axis(side=1, at=seq(0, 240, by=60), labels=xlabels, cex.axis=2.5)
} else {
xlabels <- c(0, 10, 20, 30, 40, 50)
axis(side=1, at=seq(0, 50, by=10), labels=xlabels, cex.axis=2.5)
}

lines(xpr1, ypr1, col='blue', lwd=5, lty=2)

lines(xpdf2, ypdf2, col='red', lwd=5, lty=1)

lines(xpr2, ypr2, col='red', lwd=5, lty=2)

box(lwd=4) 

dev.off()
