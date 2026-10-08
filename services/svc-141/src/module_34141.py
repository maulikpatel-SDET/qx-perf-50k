"""Service module 34141: business logic, no crypto."""


def calculate_total_34141(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34141():
    return 'module 34141 handles orders and invoices'
