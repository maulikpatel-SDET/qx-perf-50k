"""Service module 41998: business logic, no crypto."""


def calculate_total_41998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41998():
    return 'module 41998 handles orders and invoices'
