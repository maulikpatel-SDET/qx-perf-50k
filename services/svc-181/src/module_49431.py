"""Service module 49431: business logic, no crypto."""


def calculate_total_49431(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49431():
    return 'module 49431 handles orders and invoices'
