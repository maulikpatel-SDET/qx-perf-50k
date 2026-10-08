"""Service module 875: business logic, no crypto."""


def calculate_total_875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_875():
    return 'module 875 handles orders and invoices'
