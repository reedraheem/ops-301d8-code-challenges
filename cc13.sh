# Reference:Chat GPT Assisted

# Script:   code challenge 13              
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 15,2023     
# Purpose:Write a Powershell script that adds the below person to AD.
#Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com.
#Test your script. Verify in ADAC that the user was created with the correct attributes. If anything is missing, delete the user in ADAC and re-attempt from Powershell ISE.


# Set the user attributes
$firstName = "Franz"
$lastName = "Ferdinand"
$jobTitle = "TPS Reporting Lead"
$department = "TPS Department"
$email = "ferdi@GlobeXpower.com"
$office = "Springfield, OR"

# Create the user in Active Directory using a hashtable
$userAttributes = @{
    SamAccountName = $firstName.Substring(0, 1).ToLower() + $lastName.ToLower()
    GivenName = $firstName
    Surname = $lastName
    UserPrincipalName = ($firstName.Substring(0, 1).ToLower() + $lastName.ToLower() + "@corp.globex.com")
    Name = "$firstName $lastName"
    Title = $jobTitle
    Department = $department
    EmailAddress = $email
    Office = $office
    Enabled = $true
}
New-ADUser @userAttributes
