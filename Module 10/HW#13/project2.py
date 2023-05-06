#Person class w/ attributes: name, address, telephone number
#Customer = subclass of Person w/ attributes: customer num, mailing list (0/1)
#demonstrate instance of Customer class
import person

def main():
    customer1 = person.Customer('FN LN','1234 Any Ave, Los Angeles CA 90034',1234567890,1,1)
    customer1.PrintInformation()

main()