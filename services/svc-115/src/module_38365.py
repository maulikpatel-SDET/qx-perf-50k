"""Service module 38365: business logic, no crypto."""


def calculate_total_38365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38365():
    return 'module 38365 handles orders and invoices'
