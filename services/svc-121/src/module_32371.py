"""Service module 32371: business logic, no crypto."""


def calculate_total_32371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32371():
    return 'module 32371 handles orders and invoices'
