"""Service module 39677: business logic, no crypto."""


def calculate_total_39677(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39677():
    return 'module 39677 handles orders and invoices'
