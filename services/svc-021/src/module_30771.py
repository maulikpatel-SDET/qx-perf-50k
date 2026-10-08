"""Service module 30771: business logic, no crypto."""


def calculate_total_30771(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30771():
    return 'module 30771 handles orders and invoices'
