name_month = [
    'JAN', 'FAB', 'MAR', 'APR', 'MAY', 'JUN',
    'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC',
]
QUESTION = 'How much is your income for'

# tax rate for the first to seventh steps
fir_st_tax = 0.1
sec_st_tax = 0.15
thi_st_tax = 0.25
fou_st_tax = 0.28
fif_st_tax = 0.33
six_st_tax = 0.35
sev_st_tax= 0.396

# maximum amount of income for the first to seventh step for one subject
fir_st_fon = 9075
sec_st_fon = 36900
thi_st_fon = 89350
fou_st_fon = 186350
fif_st_fon = 405100
six_st_fon = 406750

# total tax amount for the first to seventh step for one subject
fir_full_fon = 907.5
sec_full_fon = 5081.25
thi_full_fon = 18193.75
fou_full_fon = 45353.75
fif_full_fon = 117541.25
six_full_fon = 118118.75

# maximum amount of income for the first to seventh step for married couple
fir_st_fmar = 18150
sec_st_fmar = 73800
thi_st_fmar = 148850
fou_st_fmar = 226850
fif_st_fmar = 405100
six_st_fmar = 457600

# total tax amount for the first to seventh step for married couple
fir_full_fmar = 1815
sec_full_fmar = 10162.5
thi_full_fmar = 28925
fou_full_fmar = 50765
fif_full_fmar = 109587.5
six_full_fmar = 127962.5

# maximum amount of income for the first to seventh step for single parent
fir_st_fsg = 12950
sec_st_fsg = 49400
thi_st_fsg = 127550
fou_st_fsg = 206600
fif_st_fsg = 405100
six_st_fsg = 432200

# total tax amount for the first to seventh step for single parent
fir_full_fsg = 1295
sec_full_fsg = 6762.35
thi_full_fsg = 26299.85
fou_full_sg = 48433.85
fif_full_sg = 113938.85
six_full_sg = 123423.5

TXT_HELLO1 = 'Hello, this program allows to calculate ' \
            'annual tax of the subject of taxation on American system.'
TXT_HELLO2 = 'The taxable amount of money changes depending' \
             ' on the particular taxation.'
TXT_HELLO3 = 'Please, write your monthly income.'
TXT_SUB = 'Which subject of taxation do you belong to?' \
          ' (one subject, married couple or single parent)\n'
TXT_COR_SUB = 'Please, write subject of taxation correctly.'
TXT_TAX_DED = 'How much is your the tax deduction:\n'
TXT_TOTAl = 'Your annual tax is:\n'
TXT_COR_DED = 'Please, write your tax deduction correctly.\n'