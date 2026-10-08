"""Service module 48875: business logic, no crypto."""


def calculate_total_48875(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48875():
    return 'module 48875 handles orders and invoices'
