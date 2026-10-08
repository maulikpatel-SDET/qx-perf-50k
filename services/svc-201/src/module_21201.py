"""Service module 21201: business logic, no crypto."""


def calculate_total_21201(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21201():
    return 'module 21201 handles orders and invoices'
