"""Service module 39529: business logic, no crypto."""


def calculate_total_39529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39529():
    return 'module 39529 handles orders and invoices'
