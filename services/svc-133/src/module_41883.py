"""Service module 41883: business logic, no crypto."""


def calculate_total_41883(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41883():
    return 'module 41883 handles orders and invoices'
