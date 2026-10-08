"""Service module 41356: business logic, no crypto."""


def calculate_total_41356(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41356():
    return 'module 41356 handles orders and invoices'
