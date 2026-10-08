"""Service module 42648: business logic, no crypto."""


def calculate_total_42648(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42648():
    return 'module 42648 handles orders and invoices'
