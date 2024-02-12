import time

print('Welcome to Otan Day 2021')
time.sleep(4)

print('Please wait...')
time.sleep(4)

sn=input('Surname: ')
sx=input('sex: ')
ms=input('Marital status...(Single/Married): ')
time.sleep(3)

if sx=='m':
    print('Welcome, Mr ' + sn)
elif sx=='f' and ms=='Single':
    print('Welcome, Miss ' +sn)
elif sx=='f' and ms=='Married':
    print('Welcome Mrs ' + sn)
else:
    print('Error...Please recheck your inputs')
    time.sleep(5)


print('Create account')
print('Please wait...')
time.sleep(6)
if sx=='m':
    print('Mr ' + sn + ' kindly provide your biodata respectively')
elif sx=='f' and ms=='Single':
    print('Miss ' + sn + ' kindly provide your biodata respectively')
elif sx=='f' and ms=='Married':
    print('Mrs ' + sn + ' kindly provide your biodata respectively')
else:
    print('Error...Please check your inputs')


#list of Ogbons
oak='Akoko'
oar='Aro'
opl='Peletu'
oyo='Oyo'
org='Orangun'
oin='Inisha'
ois='Isasawo'
oro='Iro'
ong='Onigbo'
oel='Elemu'
oid='Idofin'
owa='Owa'
ibj='imojigbon'
oro='orolu'
iba='ibayan'
owl='owalemu'


#list of streets
ii='Isale idofin'
idf='Idofin'
io='Isale obale'
oa='Oke anaye'
pc='Palace/Complex'
oo='oke-omi'
ik='Ikotun'
idg='idi ogun'
ibl='ile obala'
omr='Omi eran'
imj='Imojigbon'
oki='Oke iro'
imo='imojigbon'
oky='Oke anaye'
ryl='Royal Estate'
sas='Sasala'



#List of surnames
adb='Adebayo'
oyb='oyebade'
olw='Olawale'
oyg='Oyaguna'
ilr='Ilori'
ogw='Ogunwole'
ppl='Popoola'
ban='Bankole'
ajl='Ajala'
arl='Areola'
oke='Oke'
ain='Aina'
fad='Fadipe'
afb='Afolabi'
oni='Oni'
fat='Fatoki'
ady='Adeyemi'
iby='Ibitayo'
alb='Alabi'
ayd='Ayandare'
ayr=' Ayandiran'
ola='Oladosu'
ogd='Ogundipe'
adj='Ayandoja'
bbl='Babalola'
ode='Odeyinka'
oly='Olayiwola'
fak='Fakeye'
sal='salako'
omi='omirinde'
omr='omirinde'
ode='odeyale'
fab='fabunmi'
opa='oparinde'
abu='abulude'
aby='abuyide'
dad='dada'
fag='fagbure'
abd='abduranman'
fal='faleye'
fag='fagbemi'
fad='fadipe'
ogu='ogunleye'
ade='adeogun'
ola='olagunju'
oke='okeyode'
ogu='ogundele'
ogn='ogunniyi'
ogo='ogunjobi'
kay='kayode'
ibr='ibrahim'
ade='adewunmi'
oye='oyewo'
oyt='oyatola'
dur='durojola'
tej='tejumola'
ode='odeyinka'
aji='ajibade'
oya='oyagbona'
ola='olaifa'
sul='sule'
aji='ajiteru'
ogu='ogunjobi'

#compound names

iaro='Ile Aro'
iawo='Ile Aworogun'

#political wards
w1='Ward 1'
w2='ward 2'
w3='ward 3'




on=input('other name: ')

dob=input('D.O.B(dd/mm/yy): ')

nn=input('Nationality: ')

st=input('State: ')
if st=='Osun':
    print('Ipinle Omoluabi')

lg=input('Local Government: ')

tw=input('Town: ')

strt=input('Street name: ')

noo=input('Name Of Ogbon: ')

if sn==arl:
    print('You are from ' + iaro + 'political ward: ' + wdo)
    
if noo==oak:
    print('Ogbon\'s street location: ' + oak)

elif noo==oar:
    print('Ogbon\'s street location: ' + idg)
    
elif noo==opl:
    print('Ogbon\'s street location: ' + oo)
    
elif noo==oyo:
    print('Ogbon\'s street location: ' + oo)
    
elif noo==org:
    print('Ogbon\'s street location: ' + oo)
    
elif noo==oin:
    print('Ogbon\'s street location: ' + oki)
elif noo==ois:
    print('Ogbon\'s street location: ' + idg)

elif noo==oro:
    print('Ogbon\'s street location: ' + pc)
    
elif noo==ong:
    print('Ogbon\'s street location: ' + oo)
    
elif noo==oel:
    print('Ogbon\'s street location: ' + idf)
    
elif noo==oid:
    print('Ogbon\'s street location: ' + idf)
    
elif noo==owa:
    print('Ogbon\'s street location: ' + pc)
    
elif noo==imo:
    print('Ogbon\'s street location: ' + imo)

elif noo==iba:
    print('Ogbon\'s street location: ' + pc)
elif noo==owl:
    print('Ogbon\'s street location: ' + idf)

    
    
else:
    print('You have to belong to one Ogbon')
pn=input('Phone.no: ')

em=input('E-mail: ')

oc=input('Occupation: ') 

print('Thank you ' + fn + ', You have successfully created your account')
time.sleep(2)

print('Do you wish to take our Otan day 5mins test? ')
yn=input('(Yes/No): ')





























print('Please answer the following question...')

time.sleep(2)


print('Your test start in 5secs')
time.sleep(1)
print('4secs')

time.sleep(1)
print('3secs')

time.sleep(1)
print('2secs')

time.sleep(1)
print('1secs')

time.sleep(1)
 

aq1='106'
aq2='HRM Lukman Arenibiowo'
aq3='1912'
aq4='100'
aq5='Ay & ade'
aq6='26'
aq8='3'
aq9='oak,opl,oar,owl,ois'
aq10='26'
aq11='Anglican Grammar School'
aq12='Akorede Ganiyu & Oke Oyindamola'




q1=input('How old ls Otan Ayegbaju? ')

if q1==aq1:
    print('correct')
else:
    print('You are wrong')
    
q2=input('What is the name of the present Owa of Otan? ')
if q2==aq2:
    print('correct')
else:
    print('You are wrong')

q3=input('What year was Otan founded? ')
if q3==aq3:
    print('correct')
else:
    print('You are wrong')
    
q4=input('How many Otan day has been celebrated since inception? ')
if q4==aq4:
    print('correct')

else:
    print('You are wrong')
    
q5=input('Names of the 1st Mr & Mrs Otan? ')
if q5==aq5:
    print('correct')
else:
    print('You are wrong')

q6=input('How many Ogbons exist in Otan Ayegbaju? ')    
if q6==aq6:
    print('correct')
else:
    print('You are wrong')

q7=input('How many compounds are there in Otan ? ')
if q7==aq7:
    print('correct')
else:
    print('You are wrong')
q8=input('otan has how many shrines ? ')
if q8==aq8:
    print('correct')
else:
    print('You are wrong')
q9=input('Mention five ogbon in Otan? ')    
if q9==aq9:
    print('correct')
else:
    print('You are wrong')
q10=input('Who is the first king in Otan? ')    
if q10==aq10:
    print('correct')
else:
    print('You are wrong')
q11=input('What is the first secondary school in Otan?')    
if q11==aq11:    
 print('correct')
else:
    print('You are wrong')
          
q12=input('Who are the outgoing mr and miss Otan ? ')
if q12==aq12:
    print('correct')    
else:
    print('You are wrong')









    
if q1==aq1 and q2==aq2 and q3==aq3 and q4==aq4 and q5==aq5 and q6==aq6:
    print('Your % score is 100%')
    
elif q1==aq1 and q2==aq2 and q3==aq3 and q4==aq4 and q5==aq5 and q6!=aq6:
    print('Your % score is 80%')

elif q1==aq1 and q2==aq2 and q3==aq3 and q4==aq4 and q5!=aq5 and q6!=aq6:
    print('Your % score is 60%')

elif q1==aq1 and q2==aq2 and q3==aq3 and q4!=aq4 and q5!=aq5 and q6!=aq6:
    print('Your % score is 40%')
    
elif q1==aq1 and q2==aq2 and q3!=aq3 and q4!=aq4 and q5!=aq5 and q6!=aq6:
     print('Your % score is 20%')
     
elif q1==aq1 and q2!=aq2 and q3!=aq3 and q4!=aq4 and q5!=aq5 and q6!=aq6: 
    print('Your % score is 10%')


###################3
elif q1!=aq1 and q2!=aq2 and q3!=aq3 and q4!=aq4 and q5!=aq5 and q6!=aq6:    
    print('Your % score is 0%')
 
elif q1!=aq1 and q2!=aq2 and q3!=aq3 and q4!=aq4 and q5!=aq5 and q6==aq6:    
    print('Your % score is 10%')

elif q1!=aq1 and q2!=aq2 and q3!=aq3 and q4!=aq4 and q5==aq5 and q6==aq6:    
    print('Your % score is 20%')

elif q1!=aq1 and q2!=aq2 and q3!=aq3 and q4==aq4 and q5==aq5 and q6==aq6:    
    print('Your % score is 40%')
    
elif q1!=aq1 and q2!=aq2 and q3==aq3 and q4==aq4 and q5==aq5 and q6==aq6:    
     print('Your % score is 60%')
     
elif q1!=aq1 and q2==aq2 and q3==aq3 and q4==aq4 and q5==aq5 and q6==aq6:    
    print('Your % score is 80%')
else:
    print('Try again...')
    
