"""Service module 13222: business logic, no crypto."""


def calculate_total_13222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13222():
    return 'module 13222 handles orders and invoices'
