"""Service module 35141: business logic, no crypto."""


def calculate_total_35141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35141():
    return 'module 35141 handles orders and invoices'
