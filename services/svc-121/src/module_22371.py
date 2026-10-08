"""Service module 22371: business logic, no crypto."""


def calculate_total_22371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22371():
    return 'module 22371 handles orders and invoices'
