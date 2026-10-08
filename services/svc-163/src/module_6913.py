"""Service module 6913: business logic, no crypto."""


def calculate_total_6913(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6913():
    return 'module 6913 handles orders and invoices'
