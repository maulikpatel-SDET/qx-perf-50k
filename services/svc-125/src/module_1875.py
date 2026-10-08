"""Service module 1875: business logic, no crypto."""


def calculate_total_1875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1875():
    return 'module 1875 handles orders and invoices'
