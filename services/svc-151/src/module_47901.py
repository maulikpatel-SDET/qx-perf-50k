"""Service module 47901: business logic, no crypto."""


def calculate_total_47901(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47901():
    return 'module 47901 handles orders and invoices'
