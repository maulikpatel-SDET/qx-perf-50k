"""Service module 34737: business logic, no crypto."""


def calculate_total_34737(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34737():
    return 'module 34737 handles orders and invoices'
