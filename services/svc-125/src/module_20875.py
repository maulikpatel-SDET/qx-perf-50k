"""Service module 20875: business logic, no crypto."""


def calculate_total_20875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20875():
    return 'module 20875 handles orders and invoices'
