"""Service module 49137: business logic, no crypto."""


def calculate_total_49137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49137():
    return 'module 49137 handles orders and invoices'
