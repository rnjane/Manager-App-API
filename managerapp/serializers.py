from rest_framework import serializers
from managerapp import models

class WeeklyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeeklyModel
        fields = ['name']


class WeeklySlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WeeklySlots
        fields = ['slot_name', 'assigned_time', 'weekday', 'weekly_model']


class WeekSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Week
        fields = ['week_name']


class DailySlotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DailySlots
        fields = ['slot_name', 'assigned_time', 'logged_time', 'day_name', 'week']


class MonthlyBudgetModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MonthylyBudgetModel
        fields = ['name']


class IncomeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelIncome
        fields = ['name', 'amount', 'monthly_budget_model']


class ExpenseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ModelExpense
        fields = ['name', 'amount', 'monthly_budget_model']


class MonthSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.Month
        fields = ['name']


class MonthIncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MonthIncome
        fields = ['name', 'amount', 'logged_amount', 'description', 'month']


class MonthExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MonthExpense
        fields = ['name', 'amount', 'logged_amount', 'description', 'month']