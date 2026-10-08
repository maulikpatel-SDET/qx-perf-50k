"""Service module 345: business logic, no crypto."""


def calculate_total_345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_345():
    return 'module 345 handles orders and invoices'
