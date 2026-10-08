"""Service module 7141: business logic, no crypto."""


def calculate_total_7141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7141():
    return 'module 7141 handles orders and invoices'
