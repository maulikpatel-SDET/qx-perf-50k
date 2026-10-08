"""Service module 39426: business logic, no crypto."""


def calculate_total_39426(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39426():
    return 'module 39426 handles orders and invoices'
