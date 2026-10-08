"""Service module 12806: business logic, no crypto."""


def calculate_total_12806(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12806():
    return 'module 12806 handles orders and invoices'
