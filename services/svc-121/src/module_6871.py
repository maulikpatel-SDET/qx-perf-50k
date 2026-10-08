"""Service module 6871: business logic, no crypto."""


def calculate_total_6871(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6871():
    return 'module 6871 handles orders and invoices'
