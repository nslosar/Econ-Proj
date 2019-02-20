gdp_increase = float(input("Increase GDP by? (Numbers only)"))

how_to_shift = int(input("Increase government spending (1) or decrease taxes(2)?"))

mpc = float(input("MPC:"))
spend_multiplier = 1/(1 - mpc)
tax_multiplier = float(spend_multiplier - 1)
gov_spending = float(gdp_increase/spend_multiplier)
tax_change = float(gdp_increase/tax_multiplier)
                   
if how_to_shift == 1:
    print ("1. Government spending increases by $%d." % gov_spending)
    print("2. Some of that spending becomes someone's income.  Some of it is saved. The rest is spent.")
    step_2 = (mpc * gov_spending)
    print("3. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_2))
    step_next = input("See next step? (Yes or no)")
    if step_next == "no":
        print("The process repeats and GDP increases by $%d." % gdp_increase)
    elif step_next == "Yes" or "yes":
            step_3 = (mpc * step_2)
            print("4. Some of that additional spending becomes someone's income.  Some of it is saved. The rest is spent.")
            print("5. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_3))
            step_next2 = input("See next step? (Yes or no)")
            if step_next2 == "no":
                print("The process repeats and GDP increases by $%d." % gdp_increase)
            elif step_next2 == "Yes" or "yes":
                step_4 = (mpc * step_3)
                print("6. Some of that additional spending becomes someone's income.  Some of it is saved. The rest is spent.")
                print("7. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_4))
                step_next3 = input("See next step? (Yes or no)")
                if step_next3 == "no":
                    print("The process repeats and GDP increases by $%d." % gdp_increase)
                elif step_next3 == "Yes" or "yes":
                    step_5 = (mpc * step_4)
                    print("8. Some of that additional spending becomes someone's income.  Some of it is saved. The rest is spent.")
                    print("9. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_5))
                    print("The process repeats and GDP increases by $%d." % gdp_increase)
    
                
elif how_to_shift == 2:
    print ("1. Taxes decrease by $%d." % tax_change)
    print("2. Decrease in taxes increases consumers' disposable income.  Some of that extra income is saved. The rest is spent.")
    step_2 = (mpc * tax_change)
    print("3. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_2))
    step_next = input("See next step? (Yes or no)")
    if step_next == "no":
        print("The process repeats and GDP increases by $%d." % gdp_increase)
    elif step_next == "Yes" or "yes":
            step_3 = (mpc * step_2)
            print("4. Some of that additional spending becomes someone's income.  Some of it is saved. The rest is spent.")
            print("5. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_3))
            step_next2 = input("See next step? (Yes or no)")
            if step_next2 == "no":
                print("The process repeats and GDP increases by $%d." % gdp_increase)
            elif step_next2 == "Yes" or "yes":
                step_4 = (mpc * step_3)
                print("6. Some of that additional spending becomes someone's income.  Some of it is saved. The rest is spent.")
                print("7. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_4))
                step_next3 = input("See next step? (Yes or no)")
                if step_next3 == "no":
                    print("The process repeats and GDP increases by $%d." % gdp_increase)
                elif step_next3 == "Yes" or "yes":
                    step_5 = (mpc * step_4)
                    print("8. Some of that additional spending becomes someone's income.  Some of it is saved. The rest is spent.")
                    print("9. Since MPC = %r, consumer spending increases by $%d." % (mpc, step_5))
                    print("The process repeats and GDP increases by $%d." % gdp_increase)

                
    


