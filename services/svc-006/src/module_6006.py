"""Service module 6006: business logic, no crypto."""


def calculate_total_6006(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6006():
    return 'module 6006 handles orders and invoices'
