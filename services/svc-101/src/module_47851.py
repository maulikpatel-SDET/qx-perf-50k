"""Service module 47851: business logic, no crypto."""


def calculate_total_47851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47851():
    return 'module 47851 handles orders and invoices'
