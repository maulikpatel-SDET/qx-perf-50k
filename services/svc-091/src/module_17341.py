"""Service module 17341: business logic, no crypto."""


def calculate_total_17341(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17341():
    return 'module 17341 handles orders and invoices'
