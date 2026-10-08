"""Service module 2736: business logic, no crypto."""


def calculate_total_2736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2736():
    return 'module 2736 handles orders and invoices'
