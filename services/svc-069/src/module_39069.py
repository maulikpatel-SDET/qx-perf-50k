"""Service module 39069: business logic, no crypto."""


def calculate_total_39069(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39069():
    return 'module 39069 handles orders and invoices'
