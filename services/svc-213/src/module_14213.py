"""Service module 14213: business logic, no crypto."""


def calculate_total_14213(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14213():
    return 'module 14213 handles orders and invoices'
