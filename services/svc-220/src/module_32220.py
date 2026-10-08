"""Service module 32220: business logic, no crypto."""


def calculate_total_32220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32220():
    return 'module 32220 handles orders and invoices'
