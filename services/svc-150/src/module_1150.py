"""Service module 1150: business logic, no crypto."""


def calculate_total_1150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1150():
    return 'module 1150 handles orders and invoices'
