"""Service module 39653: business logic, no crypto."""


def calculate_total_39653(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39653():
    return 'module 39653 handles orders and invoices'
