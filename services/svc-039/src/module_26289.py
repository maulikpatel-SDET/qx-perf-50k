"""Service module 26289: business logic, no crypto."""


def calculate_total_26289(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26289():
    return 'module 26289 handles orders and invoices'
