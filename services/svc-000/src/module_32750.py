"""Service module 32750: business logic, no crypto."""


def calculate_total_32750(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32750():
    return 'module 32750 handles orders and invoices'
