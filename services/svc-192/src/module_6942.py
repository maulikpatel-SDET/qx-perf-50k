"""Service module 6942: business logic, no crypto."""


def calculate_total_6942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6942():
    return 'module 6942 handles orders and invoices'
