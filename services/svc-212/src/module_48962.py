"""Service module 48962: business logic, no crypto."""


def calculate_total_48962(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48962():
    return 'module 48962 handles orders and invoices'
