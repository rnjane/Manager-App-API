from django.db import models
from django.contrib.auth.models import User

class WeeklyModel(models.Model):
    '''this class models a weekly time slots model, used in creating all weeks'''
    name = models.CharField(max_length=30)


class WeeklySlots(models.Model):
    '''this class models all time slots in a week model'''
    slot_name = models.CharField(max_length=30)
    assigned_time = models.DurationField()
    weekday = models.CharField(max_length=15)
    weekly_model = models.ForeignKey(WeeklyModel, related_name='slots', on_delete=models.CASCADE)


class Week(models.Model):
    '''this class models a week, in terms of all slots in such a week'''
    week_name = models.CharField(max_length=30)


class DailySlots(models.Model):
    '''this class models a typical day - in terms of time slots'''
    slot_name = mdoels.CharField(max_length=30)
    assigned_time = models.DurationField()
    logged_time = models.DurationField()
    day_name = models.CharField(max_length=15)
    week = models.ForeignKey(Week, related_name='daily_slots', on_delete=models.CASCADE)


class MonthylyBudgetModel(models.Model):
    '''this class models a mothly budget model, from which all months are created'''
    name = models.CharField(max_length=30)
    

class ModelIncome(models.Model):
    '''this class models an income in a monthly budget model'''
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    monthly_budget_model = models.ForeignKey(MonthylyBudgetModel, related_name='monthly_model_income', on_delete=models.CASCADE)


class MThaodelExpense(models.Model):
    '''this class models an exopense in a monthly budget model'''
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    monthly_budget_model = models.ForeignKey(MonthylyBudgetModel, related_name='monthly_model_expense', on_delete=models.CASCADE)


class Month(models.Model):
    '''This class models a certain calendar month. comprised of a name, incomes and expenses'''
    name = models.CharField(max_length=30)

class MonthIncome(models.Model):
    '''this class models an instance of an income in a particular month'''
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    logged_amount = models.DecimalField(max_digits==20, decimal_places=2)
    description = models.CharField(max_length=150)
    month = models.ForeignKey(Month, related_name='incomes', on_delete=models.CASCADE)


class MonthExpense(models.Model):
    '''this class models an instance of an expense in a particular month'''
    name = models.CharField(max_length=30)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    logged_amount = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.CharField(max_length=30)
    month = models.ForeignKey(Month, related_name='expenses', on_delete=models.CASCADE)