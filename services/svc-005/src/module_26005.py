"""Service module 26005: business logic, no crypto."""


def calculate_total_26005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26005():
    return 'module 26005 handles orders and invoices'
