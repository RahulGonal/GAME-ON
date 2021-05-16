# Importing Modules
import phonenumbers
from phonenumbers import timezone 
from phonenumbers import geocoder, carrier 

# Collecting the PhoneNumber
PhoneNumber = phonenumbers.parse((input(("Enter the PhoneNumber beginning with the Plus sign and the country code >>>> "))))

# Validating the PhoneNumber
valid = phonenumbers.is_valid_number(PhoneNumber)
print("Valid =",valid)

# Generating the Time Zone
timeZone = timezone.time_zones_for_number(PhoneNumber) 
print('Timezone = ', timeZone)

# Getting the carrier
Carrier = carrier.name_for_number(PhoneNumber, 'en') 
print("Carrier =",Carrier)

# Finding Region
Region = geocoder.description_for_number(PhoneNumber, 'en') 
print("Region = ",Region)