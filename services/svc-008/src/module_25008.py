"""Service module 25008: business logic, no crypto."""


def calculate_total_25008(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25008():
    return 'module 25008 handles orders and invoices'
