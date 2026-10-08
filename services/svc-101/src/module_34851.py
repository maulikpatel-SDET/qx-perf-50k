"""Service module 34851: business logic, no crypto."""


def calculate_total_34851(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34851():
    return 'module 34851 handles orders and invoices'
