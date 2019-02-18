library(bla)

#############
directory <- "/home/mschilling/Desktop/gbs15/scripts_zg/ind/clustered_vsearch/"

files <- list.files(directory, pattern= "vsearch_ri*")

runinf <- list()
for (i in files){
    name <- paste("runinf", i, sep= "_")
    assign(name, read.


    runinf[i] <- readLines(i)


     
for(i in 1:6) { #-- Create objects  'r.1', 'r.2', ... 'r.6' --
    nam <- paste("r", i, sep = ".")
    assign(nam, 1:i)
}
     ls(pattern = "^r..$")






#############

setwd("/home/mschilling/Desktop/gbs15/ind/clustered_vsearch/sub_centroids/2014/")

clust_cons <- read.csv("lasio_consensus_clusters.csv", header= F)
# or better: 
clust <- read.csv("lasio_paralogs2_clusters.csv", header= F)

##
hist(clust$V2, ylim= c(0, 500))
hist(clust$V3, ylim= c(0, 500))

mrgd <- merge(clust, clust_cons, by="V1") 
table(mrgd$V2.x == mrgd$V2.y) # just checking if the two counts are actually the same


