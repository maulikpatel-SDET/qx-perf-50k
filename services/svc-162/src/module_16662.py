"""Service module 16662: business logic, no crypto."""


def calculate_total_16662(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16662():
    return 'module 16662 handles orders and invoices'
