"""Service module 37875: business logic, no crypto."""


def calculate_total_37875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37875():
    return 'module 37875 handles orders and invoices'
