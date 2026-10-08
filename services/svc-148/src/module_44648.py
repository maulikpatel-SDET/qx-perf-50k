"""Service module 44648: business logic, no crypto."""


def calculate_total_44648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44648():
    return 'module 44648 handles orders and invoices'
