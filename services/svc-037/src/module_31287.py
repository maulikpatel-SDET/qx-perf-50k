"""Service module 31287: business logic, no crypto."""


def calculate_total_31287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31287():
    return 'module 31287 handles orders and invoices'
