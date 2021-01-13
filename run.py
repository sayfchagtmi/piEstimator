# Import simulation functions from utils
from utils import functions as F
import sys
# Define default iteration number    
DEFAULT_N = 10**7    
# Take iteration number as argument else take default value 10**7
try:
   n = int(sys.argv[1])
except:
   n = DEFAULT_N   

# Simulate Pi using numpy
numpy_res = F.simulate(F.pi_estimator_numpy,n)
# Simulate Pi using spark
spark_res = F.simulate(F.pi_estimator_spark,n)

#Print results 
hline = "---------------------------------------------------------------------------------------------------------"
header = "n =%s\t|\t %12s \t|\t %12s \t|\t %12s \t|" % (n,"Temps d'éxécution","Valeur de Pi","Ecart % Math.pi")
print(f'{hline}\n{header}\n{hline}\n{numpy_res}\n{hline}\n{spark_res}\n{hline}')