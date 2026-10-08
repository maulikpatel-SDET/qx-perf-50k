"""Service module 39659: business logic, no crypto."""


def calculate_total_39659(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39659():
    return 'module 39659 handles orders and invoices'
