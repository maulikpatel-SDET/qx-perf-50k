"""Service module 44875: business logic, no crypto."""


def calculate_total_44875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44875():
    return 'module 44875 handles orders and invoices'
