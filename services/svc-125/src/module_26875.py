"""Service module 26875: business logic, no crypto."""


def calculate_total_26875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26875():
    return 'module 26875 handles orders and invoices'
