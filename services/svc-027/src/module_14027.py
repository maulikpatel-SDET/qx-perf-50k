"""Service module 14027: business logic, no crypto."""


def calculate_total_14027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14027():
    return 'module 14027 handles orders and invoices'
