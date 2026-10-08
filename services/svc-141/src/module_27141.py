"""Service module 27141: business logic, no crypto."""


def calculate_total_27141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27141():
    return 'module 27141 handles orders and invoices'
