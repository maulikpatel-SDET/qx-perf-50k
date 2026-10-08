"""Service module 29942: business logic, no crypto."""


def calculate_total_29942(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29942():
    return 'module 29942 handles orders and invoices'
