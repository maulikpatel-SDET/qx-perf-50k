"""Service module 15532: business logic, no crypto."""


def calculate_total_15532(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15532():
    return 'module 15532 handles orders and invoices'
