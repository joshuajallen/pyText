# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 11:18:57 2018

@author: Zahid
"""

import camelot
import pandas as pd

exec(open("Scripts/HelperFuns.py").read())
exec(open("Scripts/getData.py").read())

nlp = en_core_web_sm.load()
nlp.max_length = 10000000

directory = 'C:\\Users\\328576\\PycharmProjects\\pyText\\TestData\\MPC'
pdf_files = get_pdf_files(directory)
print(pdf_files)
myFile = pdf_files[1]



def append_pdf_pages_in_df(x):
    
    df1 = x[0].df
    
    for i in range(1,len(x)):
        
        df_append = x[i].df
        df1 = df1.append(df_append, ignore_index=True)
        print(i)
        print(len(df1))   

    return(df1)

PRIN = camelot.read_pdf(myFile, pages= '36-37')
df_PRIN = append_pdf_pages_in_df(PRIN)
df_PRIN['Type'] = "PRIN"

SYSC = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '38-55')
df_SYSC = append_pdf_pages_in_df(SYSC)
df_SYSC['Type'] = "SYSC"

FIT = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '56')
df_FIT = append_pdf_pages_in_df(FIT)
df_FIT['Type'] = "FIT"

FINMAR = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '57-60')
df_FINMAR = append_pdf_pages_in_df(FINMAR)
df_FINMAR['Type'] = "FINMAR"

TC = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '61-67')
df_TC = append_pdf_pages_in_df(TC)
df_TC['Type'] = "TC"

FEES = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '68-91')
df_FEES = append_pdf_pages_in_df(FEES)
df_FEES['Type'] = "FEES"

GENPRU = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '92-129')
df_GENPRU = append_pdf_pages_in_df(GENPRU)
df_GENPRU['Type'] = "GENPRU"

BIPRU = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '130-263')
df_BIPRU = append_pdf_pages_in_df(BIPRU)
df_BIPRU['Type'] = "BIPRU"

INSPRU = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '264-305')
df_INSPRU = append_pdf_pages_in_df(INSPRU)
df_INSPRU['Type'] = "INSPRU"

MIPRU = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '306-312')
df_MIPRU = append_pdf_pages_in_df(MIPRU)
df_MIPRU['Type'] = "MIPRU"

UPRU = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '313')
df_UPRU = append_pdf_pages_in_df(UPRU)
df_UPRU['Type'] = "UPRU"

IPRU = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '315-334')
df_IPRU = append_pdf_pages_in_df(IPRU)
df_IPRU['Type'] = "IPRU"

IPRU_INS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '335-362')
df_IPRU_INS = append_pdf_pages_in_df(IPRU_INS) # dont upload - insurance

IPRU_INV = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '363-393')
df_IPRU_INV = append_pdf_pages_in_df(IPRU_INV)
df_IPRU_INV['Type'] = "IPRU_INV"

COBS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '394-417')
df_COBS = append_pdf_pages_in_df(COBS)
df_COBS['Type'] = "COBS"

ICOBS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '418-427')
df_ICOBS = append_pdf_pages_in_df(ICOBS) # dont upload - insurance

MCOB = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '428-454')
df_MCOB = append_pdf_pages_in_df(MCOB)
df_MCOB['Type'] = "MCOB"

BCOBS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '455-457')
df_BCOBS = append_pdf_pages_in_df(BCOBS)
df_BCOBS['Type'] = "BCOBS"

CASS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '458-468')
df_CASS = append_pdf_pages_in_df(CASS)
df_CASS['Type'] = "CASS"

MAR = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '469-475')
df_MAR = append_pdf_pages_in_df(MAR) 
df_MAR['Type'] = "MAR"

SUP = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '476-495')
df_SUP = append_pdf_pages_in_df(SUP) 
df_SUP['Type'] = "SUP"

DISP = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '496-507')
df_DISP = append_pdf_pages_in_df(DISP)
df_DISP['Type'] = "DISP"

CONRED = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '508-509')
df_CONRED = append_pdf_pages_in_df(CONRED)
df_CONRED['Type'] = "CONRED"

COMP = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '510-518')
df_COMP = append_pdf_pages_in_df(COMP)
df_COMP['Type'] = "COMP"

BSOCS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '519-522')
df_BSOCS = append_pdf_pages_in_df(BSOCS)
df_BSOCS['Type'] = "BSOCS"

COLL = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '523-538')
df_COLL = append_pdf_pages_in_df(COLL)
df_COLL['Type'] = "COLL"

CREDS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '539-544')
df_CREDS = append_pdf_pages_in_df(CREDS)
df_CREDS['Type'] = "CREDS"

PROF = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '545-546')
df_PROF = append_pdf_pages_in_df(PROF)
df_PROF['Type'] = "PROF"

RCB = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '547-550')
df_RCB = append_pdf_pages_in_df(RCB)
df_RCB['Type'] = "RCB"

LR = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '551-570')
df_LR = append_pdf_pages_in_df(LR)
df_LR['Type'] = "LR"

PR = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '571-574')
df_PR = append_pdf_pages_in_df(PR)
df_PR['Type'] = "PR"

DTR = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '575-580')
df_DTR = append_pdf_pages_in_df(DTR)
df_DTR['Type'] = "DTR"

EMPS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '581')
df_EMPS = append_pdf_pages_in_df(EMPS)
df_EMPS['Type'] = "EMPS"

OMPS = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '582')
df_OMPS = append_pdf_pages_in_df(OMPS)
df_OMPS['Type'] = "OMPS"

SERV = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '583')
df_SERV = append_pdf_pages_in_df(SERV)
df_SERV['Type'] = "SERV"

BSOG = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '584-593')
df_BSOG = append_pdf_pages_in_df(BSOG)
df_BSOG['Type'] = "BSOG"

COLLG = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '594-595')
df_COLLG = append_pdf_pages_in_df(COLLG)
df_COLLG['Type'] = "COLLG"

FC = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '596-609')
df_FC = append_pdf_pages_in_df(FC)
df_FC['Type'] = "FC"

PERG = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '610-637')
df_PERG = append_pdf_pages_in_df(PERG)
df_PERG['Type'] = "PERG"

RPPD = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '638')
df_RPPD = append_pdf_pages_in_df(RPPD)
df_RPPD['Type'] = "RPPD"

UNFCOG = camelot.read_pdf("C:/Users/Zahid/Documents/complexity/data/FCA_2013_8_PRA_2013_3.pdf", pages= '639')
df_UNFCOG = append_pdf_pages_in_df(UNFCOG)
df_UNFCOG['Type'] = "UNFCOG"


# appending all

first_extract = pd.read_pickle("C:/Users/Zahid/Documents/complexity/data/extracts_1.pkl")

fca_pra_2013 = first_extract.append(second_extract, ignore_index = True)

fca_pra_2013.to_pickle("C:/Users/Zahid/Documents/complexity/data/fca_pra_2013.pkl")

fca_pra_2013.to_csv("C:/Users/Zahid/Documents/complexity/data/fca_pra_2013.csv", sep='\t')



#################

fca_pra_2013 = pd.read_pickle("C:/Users/324910/Documents/Python Scripts/fca_pra_2013_scraped_v2.pkl")

fca_pra_2013.to_csv("C:/Users/324910/Documents/Python Scripts/fca_pra_2013_scraped_v2.csv", sep='\t')


##########################

# saving second extracts

#df_BSOCS['Type'] = "BSOCS"
#df_BSOG['Type'] = "BSOG"
#df_CASS['Type'] = "CASS"
#df_COBS['Type'] = "COBS"
#df_COLL['Type'] = "COLL"
#df_COLLG['Type'] = "COLLG"
#df_COMP['Type'] = "COMP"
#df_CONRED['Type'] = "CONRED"
#df_CREDS['Type'] = "CREDS"
#df_DISP['Type'] = "DISP"
#df_DTR['Type'] = "DTR"
#df_EMPS['Type'] = "EMPS"
#df_FC['Type'] = "FC"
#df_LR['Type'] = "LR"
#df_MAR['Type'] = "MAR"
#df_MCOB['Type'] = "MCOB"
#df_OMPS['Type'] = "OMPS"
#df_PERG['Type'] = "PERG"
#df_PR['Type'] = "PR"
#df_PROF['Type'] = "PROF"
#df_RCB['Type'] = "RCB"
#df_RPPD['Type'] = "RPPD"
#df_SERV['Type'] = "SERV"
#df_SUP['Type'] = "SUP"
#df_UNFCOG['Type'] = "UNFCOG"
#
#
#second_extract = df_BSOCS.append([df_BSOCS, df_BSOG, df_CASS, df_COBS, df_COLL, df_COLLG, df_COMP, df_CONRED, df_CREDS, df_DISP, df_DTR, df_EMPS, df_FC, df_LR, df_MAR, df_MCOB, df_OMPS, df_PERG, df_PR, df_PROF, df_RCB, df_RPPD, df_SERV, df_SUP, df_UNFCOG])
#
#second_extract.to_csv("C:/Users/Zahid/Documents/complexity/data/extracts_2.csv", sep='\t')
#
#second_extract.to_pickle("C:/Users/Zahid/Documents/complexity/data/extracts_2.pkl")
#
## saving first extracts
#df_BCOBS['Type'] = "BCOBS"
#df_BIPRU['Type'] = "BIPRU"
#df_FEES['Type'] = "FEES"
#df_FINMAR['Type'] = "FINMAR"
#df_FIT['Type'] = "FIT"
#df_GENPRU['Type'] = "GENPRU"
#df_IPRU['Type'] = "IPRU"
#df_IPRU_INV['Type'] = "IPRU_INV"
#df_MIPRU['Type'] = "MIPRU"
#df_PRIN['Type'] = "PRIN"
#df_SYSC['Type'] = "SYSC"
#df_TC['Type'] = "TC"
#df_UPRU['Type'] = "UPRU"
#
#
#to_save = df_BCOBS.append([df_BIPRU, df_FEES, df_FINMAR, df_FIT, df_GENPRU, df_IPRU, df_IPRU_INV, df_MIPRU, df_PRIN, df_SYSC, df_TC, df_UPRU], ignore_index = True)
#
#to_save.to_csv("C:/Users/Zahid/Documents/complexity/data/extracts_1.csv", sep='\t')
#
#to_save.to_pickle("C:/Users/Zahid/Documents/complexity/data/extracts_1.pkl")

