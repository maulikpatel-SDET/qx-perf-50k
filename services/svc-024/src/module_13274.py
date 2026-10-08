"""Service module 13274: business logic, no crypto."""


def calculate_total_13274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13274():
    return 'module 13274 handles orders and invoices'
