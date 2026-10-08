"""Service module 3160: business logic, no crypto."""


def calculate_total_3160(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3160():
    return 'module 3160 handles orders and invoices'
