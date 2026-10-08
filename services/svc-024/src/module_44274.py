"""Service module 44274: business logic, no crypto."""


def calculate_total_44274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44274():
    return 'module 44274 handles orders and invoices'
