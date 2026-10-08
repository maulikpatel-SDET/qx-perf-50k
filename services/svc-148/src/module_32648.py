"""Service module 32648: business logic, no crypto."""


def calculate_total_32648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32648():
    return 'module 32648 handles orders and invoices'
