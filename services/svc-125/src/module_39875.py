"""Service module 39875: business logic, no crypto."""


def calculate_total_39875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39875():
    return 'module 39875 handles orders and invoices'
