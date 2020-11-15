# Case-study #2
# Developers:   Kostylev M. (40%),
#               Turchinovich M. (35%),
#               Zubareva T. (35%).
# This program allows to calculate annual tax of the subject of taxation on American system.
# The taxable amount of money changes depending on the particular taxation.

import per as p

# String constants
annual_income = 0

# Taxpayer income for each month
print(p.TXT_HELLO1, p.TXT_HELLO2, p.TXT_HELLO3, sep='\n')
for month in range(12):
    print('{} {}:'.format(p.QUESTION, p.name_month[month], end=''))
    income = float(input())
    annual_income += income
print('annual_income is:\n', annual_income, '$', sep='')

# Checking for correctness of the entered information
if annual_income <= 0:
    print('Please, restart the program and write your real income.')
# Calculation annual income with out tax deduction
else:
    tax_deduction = float(input(p.TXT_TAX_DED))
    while tax_deduction >= annual_income:
        tax_deduction = float(input(p.TXT_COR_DED))
    annual_income -= tax_deduction
    print('Taxable amount:\n', annual_income, '$', sep='')
    sub_of_tax = str(input(p.TXT_SUB)).lower().strip()
    while not (sub_of_tax == 'one subject' or
               sub_of_tax == 'married couple'
               or sub_of_tax == 'single parent'):
        print(p.TXT_COR_SUB)

    # Checking and calculating the tax amount for one subject
    if sub_of_tax == 'one subject':
        if annual_income <= p.fir_st_fon:                        # Comparison annual income with first stage
            tax_amount = annual_income * p.fir_st_tax            # Calculate taxable amount for third stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fir_st_fon < annual_income <= p.sec_st_fon:       # Comparison annual income with first and second stage
            tax_amount = (annual_income - p.fir_st_fon) \
                     * p.sec_st_tax + p.fir_full_fon             # Calculate taxable amount for second stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.sec_st_fon < annual_income <= p.thi_st_fon:       # Comparison annual income with second and third stage
            tax_amount = (annual_income - p.sec_st_fon) \
                     * p.thi_st_tax + p.sec_full_fon             # Calculate taxable amount for third stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.thi_st_fon < annual_income <= p.fou_st_fon:       # Comparison annual income with third and fourth stage
            tax_amount = (annual_income - p.thi_st_fon) \
                     * p.fou_st_tax + p.thi_full_fon             # Calculate taxable amount for fourth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fou_st_fon < annual_income <= p.fif_st_fon:       # Comparison annual income with fourth and fifth stage
            tax_amount = (annual_income - p.fou_st_fon) \
                     * p.fif_st_tax + p.fou_full_fon             # Calculate taxable amount for fifth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fif_st_fon < annual_income <= p.six_st_fon:       # Comparison annual income with fifth and sixth stage
            tax_amount = (annual_income - p.fif_st_fon) \
                     * p.six_st_tax + p.fif_full_fon             # Calculate taxable amount for sixth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif annual_income > p.six_st_fon:                       # Comparison annual income with seventh stage
            tax_amount = (annual_income - p.six_st_fon) \
                     * p.sev_st_tax + p.six_full_fon             # Calculate taxable amount for seventh stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')

    # Checking and calculating the tax amount for married couple
    elif sub_of_tax == 'married couple':
        if annual_income <= p.fir_st_fmar:                       # Comparison annual income with first stage
            tax_amount = annual_income * p.fir_st_tax            # Calculate taxable amount for third stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fir_st_fmar < annual_income <= p.sec_st_fmar:     # Comparison annual income with first and second stage
            tax_amount = (annual_income - p.fir_st_fmar) \
                     * p.sec_st_tax + p.fir_full_fmar            # Calculate taxable amount for second stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.sec_st_fmar < annual_income <= p.thi_st_fmar:     # Comparison annual income with second and third stage
            tax_amount = (annual_income - p.sec_st_fmar) \
                     * p.thi_st_tax + p.sec_full_fmar            # Calculate taxable amount for third stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.thi_st_fmar < annual_income <= p.fou_st_fmar:     # Comparison annual income with third and fourth stage
            tax_amount = (annual_income - p.thi_st_fmar) \
                     * p.fou_st_tax + p.thi_full_fmar            # Calculate taxable amount for fourth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fou_st_fmar < annual_income <= p.fif_st_fmar:     # Comparison annual income with fourth and fifth stage
            tax_amount = (annual_income - p.fou_st_fon) \
                     * p.fif_st_tax + p.fou_full_fmar            # Calculate taxable amount for fifth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fif_st_fmar < annual_income <= p.six_st_fmar:     # Comparison annual income with fifth and sixth stage
            tax_amount = (annual_income - p.fif_st_fmar) \
                     * p.six_st_tax + p.fif_full_fmar            # Calculate taxable amount for sixth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif annual_income > p.six_st_fmar:                      # Comparison annual income with seventh stage
            tax_amount = (annual_income - p.six_st_fmar) \
                     * p.sev_st_tax + p.six_full_fmar            # Calculate taxable amount for seventh stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')

    # Checking and calculating the tax amount for single parent
    elif sub_of_tax == 'single parent':
        if annual_income <= p.fir_st_fsg:                        # Comparison annual income with first stage
            tax_amount = annual_income * p.fir_st_tax            # Calculate taxable amount for third stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fir_st_fsg < annual_income <= p.sec_st_fsg:       # Comparison annual income with first and second stage
            tax_amount = (annual_income - p.fir_st_fsg) \
                     * p.sec_st_tax + p.fir_full_fsg             # Calculate taxable amount for second stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.sec_st_fsg < annual_income <= p.thi_st_fsg:       # Comparison annual income with second and third stage
            tax_amount = (annual_income - p.sec_st_fsg) \
                     * p.thi_st_tax + p.sec_full_fsg             # Calculate taxable amount for third stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.thi_st_fsg < annual_income <= p.fou_st_fsg:       # Comparison annual income with third and fourth stage
            tax_amount = (annual_income - p.thi_st_fon) \
                     * p.fou_st_tax + p.thi_full_fsg             # Calculate taxable amount for fourth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fou_st_fsg < annual_income <= p.fif_st_fon:       # Comparison annual income with fourth and fifth stage
            tax_amount = (annual_income - p.fou_st_fsg) \
                     * p.fif_st_tax + p.fou_full_sg              # Calculate taxable amount for fifth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif p.fif_st_fsg < annual_income <= p.six_st_fsg:       # Comparison annual income with fifth and sixth stage
            tax_amount = (annual_income - p.fif_st_fsg) \
                     * p.six_st_tax + p.fif_full_sg              # Calculate taxable amount for sixth stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')
        elif annual_income > p.six_st_fsg:                       # Comparison annual income with seventh stage
            tax_amount = (annual_income - p.six_st_fsg) \
                     * p.sev_st_tax + p.six_full_sg              # Calculate taxable amount for seventh stage
            print(p.TXT_TOTAl, tax_amount, '$', sep='')