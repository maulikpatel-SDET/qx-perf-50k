"""Service module 37160: business logic, no crypto."""


def calculate_total_37160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37160():
    return 'module 37160 handles orders and invoices'
