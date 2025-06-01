#  WAP to fill in a letter template given below with name and date. 
letter = ''' Dear <|NAME|> ,
you are selected !
<DATE>'''

print (letter.replace("<|NAME|>","Tiwari_Ji").replace("<DATE>","1 June 2025"))