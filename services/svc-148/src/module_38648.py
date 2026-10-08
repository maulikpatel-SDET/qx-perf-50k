"""Service module 38648: business logic, no crypto."""


def calculate_total_38648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38648():
    return 'module 38648 handles orders and invoices'
