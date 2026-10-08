"""Service module 4648: business logic, no crypto."""


def calculate_total_4648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4648():
    return 'module 4648 handles orders and invoices'
