balance = 500
withdrawal_amount = 200
has_withdrawal_permission = True

if balance >= withdrawal_amount:
    if has_withdrawal_permission:
        print("Withdrawal successful.")
    else:
        print("You do not have permission to make a withdrawal.")
else:
    print("Insufficient balance for withdrawal.")
