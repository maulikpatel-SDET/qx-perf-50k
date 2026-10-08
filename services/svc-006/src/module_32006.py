"""Service module 32006: business logic, no crypto."""


def calculate_total_32006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32006():
    return 'module 32006 handles orders and invoices'
