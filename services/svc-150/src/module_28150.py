"""Service module 28150: business logic, no crypto."""


def calculate_total_28150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28150():
    return 'module 28150 handles orders and invoices'
