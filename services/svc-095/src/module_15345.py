"""Service module 15345: business logic, no crypto."""


def calculate_total_15345(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15345():
    return 'module 15345 handles orders and invoices'
