"""Service module 47371: business logic, no crypto."""


def calculate_total_47371(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47371():
    return 'module 47371 handles orders and invoices'
