"""Service module 37371: business logic, no crypto."""


def calculate_total_37371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37371():
    return 'module 37371 handles orders and invoices'
