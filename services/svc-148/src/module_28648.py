"""Service module 28648: business logic, no crypto."""


def calculate_total_28648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28648():
    return 'module 28648 handles orders and invoices'
