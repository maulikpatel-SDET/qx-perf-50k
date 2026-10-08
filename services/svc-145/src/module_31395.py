"""Service module 31395: business logic, no crypto."""


def calculate_total_31395(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31395():
    return 'module 31395 handles orders and invoices'
