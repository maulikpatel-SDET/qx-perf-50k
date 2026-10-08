"""Service module 30340: business logic, no crypto."""


def calculate_total_30340(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30340():
    return 'module 30340 handles orders and invoices'
