from abc import ABC


class Bank(ABC):
    total_bank_balance = 0
    total_loan_amount = 0
    isLoanFeatureOn = True

    def _update_total_bank_balance(self, amount):
        self.total_bank_balance += amount
        return self.total_bank_balance

    def _update_total_loan_amount(self, amount):
        self.total_loan_amount += amount
        return self.total_loan_amount

    def _toggle_loan_feature(self):
        if self.isLoanFeatureOn is True:
            self.isLoanFeatureOn = False
        else:
            self.isLoanFeatureOn = True
        return self.isLoanFeatureOn
