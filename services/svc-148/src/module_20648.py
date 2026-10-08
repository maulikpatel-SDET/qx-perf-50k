"""Service module 20648: business logic, no crypto."""


def calculate_total_20648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20648():
    return 'module 20648 handles orders and invoices'
