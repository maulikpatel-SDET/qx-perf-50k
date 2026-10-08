"""Service module 9137: business logic, no crypto."""


def calculate_total_9137(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9137():
    return 'module 9137 handles orders and invoices'
