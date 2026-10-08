"""Service module 24274: business logic, no crypto."""


def calculate_total_24274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24274():
    return 'module 24274 handles orders and invoices'
