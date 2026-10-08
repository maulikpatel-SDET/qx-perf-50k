"""Service module 4709: business logic, no crypto."""


def calculate_total_4709(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4709():
    return 'module 4709 handles orders and invoices'
