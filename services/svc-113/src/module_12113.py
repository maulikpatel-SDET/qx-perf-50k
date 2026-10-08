"""Service module 12113: business logic, no crypto."""


def calculate_total_12113(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12113():
    return 'module 12113 handles orders and invoices'
