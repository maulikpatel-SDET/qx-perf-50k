"""Service module 10648: business logic, no crypto."""


def calculate_total_10648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10648():
    return 'module 10648 handles orders and invoices'
