"""Service module 40201: business logic, no crypto."""


def calculate_total_40201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40201():
    return 'module 40201 handles orders and invoices'
