from pyscript import document, display

def grab_average(e):
    # Grabs all the values of each subject
    math = int(document.getElementById("math").value)
    science = int(document.getElementById("science").value)
    english = int(document.getElementById("english").value)
    filipino = int(document.getElementById("filipino").value)
    
    # Calculates the average
    avrg = (math + science + english + filipino) / 4
    document.getElementById("output").innerHTML = "" # Clears the previous output if any

    display(f"Average: {avrg}", target="output")
    # Decides if the average is passing or not
    if avrg > 74:
        display("Passed? Yes", target="output")
    else:
        display("Passed? No", target="output")
