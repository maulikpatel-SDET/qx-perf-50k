"""Service module 36942: business logic, no crypto."""


def calculate_total_36942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36942():
    return 'module 36942 handles orders and invoices'
