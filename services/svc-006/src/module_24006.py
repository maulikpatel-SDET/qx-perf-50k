"""Service module 24006: business logic, no crypto."""


def calculate_total_24006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24006():
    return 'module 24006 handles orders and invoices'
