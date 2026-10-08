"""Service module 41274: business logic, no crypto."""


def calculate_total_41274(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41274():
    return 'module 41274 handles orders and invoices'
