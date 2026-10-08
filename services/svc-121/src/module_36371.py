"""Service module 36371: business logic, no crypto."""


def calculate_total_36371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36371():
    return 'module 36371 handles orders and invoices'
