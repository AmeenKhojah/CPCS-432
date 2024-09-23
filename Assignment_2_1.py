import jpype
import jpype.imports
from jpype.types import *


jpype.startJVM(classpath=["C:/Users/Amin/Desktop/ArabiTools-1.2.0.jar"]) #Your path for the jar file


# Import the Java classes
from arabi.tools.words.expan import Expander


expander = Expander()


word = "طموح" #Input desired word


derivatives = expander.getExpandByRoot(word, 0, True)


print(derivatives)


jpype.shutdownJVM()
