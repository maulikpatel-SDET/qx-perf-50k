"""Service module 5875: business logic, no crypto."""


def calculate_total_5875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5875():
    return 'module 5875 handles orders and invoices'
