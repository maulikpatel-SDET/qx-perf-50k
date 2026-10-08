"""Service module 24220: business logic, no crypto."""


def calculate_total_24220(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24220():
    return 'module 24220 handles orders and invoices'
