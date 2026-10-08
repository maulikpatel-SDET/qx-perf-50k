"""Service module 39648: business logic, no crypto."""


def calculate_total_39648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39648():
    return 'module 39648 handles orders and invoices'
