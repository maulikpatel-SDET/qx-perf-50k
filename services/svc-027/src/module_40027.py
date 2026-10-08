"""Service module 40027: business logic, no crypto."""


def calculate_total_40027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40027():
    return 'module 40027 handles orders and invoices'
