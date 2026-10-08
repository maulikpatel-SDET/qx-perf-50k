"""Service module 23137: business logic, no crypto."""


def calculate_total_23137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23137():
    return 'module 23137 handles orders and invoices'
