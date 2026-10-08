"""Service module 16155: business logic, no crypto."""


def calculate_total_16155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16155():
    return 'module 16155 handles orders and invoices'
