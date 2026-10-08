"""Service module 39913: business logic, no crypto."""


def calculate_total_39913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39913():
    return 'module 39913 handles orders and invoices'
