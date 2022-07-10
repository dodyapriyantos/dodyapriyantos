import numpy


#fill all vector to empty or zeros
NumpyPracticeEmpty = numpy.empty(10)
print ("numpy.empty(10) = " +str(NumpyPracticeEmpty))

#fill all vector to zeros
NumpyPracticeZeros = numpy.zeros(11)
print ("numpy.zeros(11) =" + str(NumpyPracticeZeros))

#fill all vector to empty or ones
NumpyPracticeOnes = numpy.ones(12)
print ("numpy.ones(12) =" + str(NumpyPracticeOnes))

#create array and fill it
NumpyPracticeArray = numpy.array([0,1,2,3,4,5,6,7,8,9])
print ("NumpyPracticeArray =" + str(NumpyPracticeArray))
print ("NumpyPracticeArray[2] = "+ str(NumpyPracticeArray[2]))
print ("numpy.mean(NumpyPracticeArray) = " + str(numpy.mean(NumpyPracticeArray)))
print ("numpy.max(NumpyPracticeArray) = " + str(numpy.max(NumpyPracticeArray)))
print ("numpy.min(NumpyPracticeArray) = " + str(numpy.min(NumpyPracticeArray)))
print ("numpy.average(NumpyPracticeArray) = " + str(numpy.average(NumpyPracticeArray)))
print ("numpy.std(NumpyPracticeArray) = " + str(numpy.std(NumpyPracticeArray)))
print ("numpy.nanstd(NumpyPracticeArray) = " + str(numpy.nanstd(NumpyPracticeArray)))
print ("numpy.median(NumpyPracticeArray) = " + str(numpy.median(NumpyPracticeArray)))
print ("numpy.nanmedian(NumpyPracticeArray) = " + str(numpy.nanmedian(NumpyPracticeArray)))
print ("numpy.var(NumpyPracticeArray) = " + str(numpy.var(NumpyPracticeArray)))
print ("numpy.nanvar(NumpyPracticeArray) = " + str(numpy.nanvar(NumpyPracticeArray)))
print ()

#create and fill a random array
rng = numpy.random.default_rng()
NumpyPracticeArray = rng.integers(10, size=100)
print ("NumpyPracticeArray =" + str(NumpyPracticeArray))
print ("NumpyPracticeArray[2] = "+ str(NumpyPracticeArray[2]))
print ("numpy.mean(NumpyPracticeArray) = " + str(numpy.mean(NumpyPracticeArray)))
print ("numpy.max(NumpyPracticeArray) = " + str(numpy.max(NumpyPracticeArray)))
print ("numpy.min(NumpyPracticeArray) = " + str(numpy.min(NumpyPracticeArray)))
print ("numpy.average(NumpyPracticeArray) = " + str(numpy.average(NumpyPracticeArray)))
print ("numpy.std(NumpyPracticeArray) = " + str(numpy.std(NumpyPracticeArray)))
print ("numpy.nanstd(NumpyPracticeArray) = " + str(numpy.nanstd(NumpyPracticeArray)))
print ("numpy.median(NumpyPracticeArray) = " + str(numpy.median(NumpyPracticeArray)))
print ("numpy.nanmedian(NumpyPracticeArray) = " + str(numpy.nanmedian(NumpyPracticeArray)))
print ("numpy.var(NumpyPracticeArray) = " + str(numpy.var(NumpyPracticeArray)))
print ("numpy.nanvar(NumpyPracticeArray) = " + str(numpy.nanvar(NumpyPracticeArray)))
print ()