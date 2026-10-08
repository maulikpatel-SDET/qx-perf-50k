"""Service module 44287: business logic, no crypto."""


def calculate_total_44287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44287():
    return 'module 44287 handles orders and invoices'
