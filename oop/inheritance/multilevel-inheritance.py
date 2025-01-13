# Multi Lavel Inheritance 

class ImportClass:
    def __init__(self, importID, invoiceNO, date, location):
        self.importID = importID
        self.invoiceNO = invoiceNO
        self.date = date
        self.location = location
    
    # return function
    def displayInvoice(self):
        print(f"Import ID:{self.importID}\nInvoice NO: {self.invoiceNO}\nDate: {self.date}\nAddress: {self.location}")

class InventoryClass(ImportClass):
    def __init__(self, importID, invoiceNO, date, location, stock):
        self.importID 

# Create object 
importOne =  ImportClass("P0001", "IN001" , "13/01/2025" , "Dhaka, Bangladesh")
importOne.displayInvoice()
