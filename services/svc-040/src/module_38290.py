"""Service module 38290: business logic, no crypto."""


def calculate_total_38290(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38290():
    return 'module 38290 handles orders and invoices'
