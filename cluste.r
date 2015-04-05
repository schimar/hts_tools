library(bla)

#############
directory <- "/home/mschilling/Desktop/gbs15/scripts_zg/ind/clustered_vsearch/"

files <- list.files(directory, pattern= "vsearch_ri*")

runinf <- list()
for (i in files){
    name <- paste("runinf", i, sep= "_")
    assign(name, read.


    runinf[i] <- readLines(i)
}

     
for(i in 1:6) { #-- Create objects  'r.1', 'r.2', ... 'r.6' --
    nam <- paste("r", i, sep = ".")
    assign(nam, 1:i)
}
     ls(pattern = "^r..$")
















