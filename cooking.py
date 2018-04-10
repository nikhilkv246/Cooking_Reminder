"""
* cooking.py
*  A python application that reminds you of your cooking turns.
*
*  @author Nikhil KV
*  @version 04102018
*
"""
import warnings                                                                                                     
import smtplib                                                                                                      
from datetime import date                                                                                           
import calendar                                                                                                     
from email.MIMEMultipart import MIMEMultipart                                                                       
from email.MIMEText import MIMEText                                                                                 
                                                                                                                    
my_date = date.today()                                                                                              
day = calendar.day_name[my_date.weekday()]                                                                          
#print(day)                                                                                                         
mapn = {'Monday':'Chandrakanth','Tuesday':'Nikhil','Wednesday':'Kiran','Thursday':'Sachin','Friday':'Suhas','Sunday':'Naveen'}                                                                                                          
mape = {'Chandrakanth':'chandrakanth.cbpur@gmail.com','Nikhil':'nikhilkv246@gmail.com','Kiran':'kiranpv9085@gmail.com','Sachin':'Sachinsp14@gmail.com','Suhas':'suhasjanardhan@gmail.com','Naveen':'naveenkumarbr111@gmail.com'}        
print(mapn[day])                                                                                                    
print(mape[mapn[day]])                                                                                              
                                                                                                                    
                                                                                                                    
fromaddr = "cahill4413boys@gmail.com"                                                                               
toaddr = mape[mapn[day]]                                                                                            
                                                                                                                    
msg = MIMEMultipart()                                                                                               
msg['From'] = fromaddr                                                                                              
msg['To'] = toaddr                                                                                                  
msg['Subject'] = "It's your turn to cook!!"                                                                         
name = mapn[day]                                                                                                    
body = "Hey %s,\n\nLooks like its your cooking turn today. Why don't you cook us some yummy food?!!\n\nThanks,\nCahill Boys" % name                                                                                                     
msg.attach(MIMEText(body, 'plain'))                                                                                 
                                                                                                                    
server = smtplib.SMTP('smtp.gmail.com', 587)                                                                        
server.starttls()                                                                                                   
server.login(fromaddr, "give_your_email_password")                                                                                
text = msg.as_string()                                                                                              
server.sendmail(fromaddr, toaddr, text)                                                                             
server.quit()
