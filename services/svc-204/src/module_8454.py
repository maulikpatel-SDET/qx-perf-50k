"""Service module 8454: business logic, no crypto."""


def calculate_total_8454(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8454():
    return 'module 8454 handles orders and invoices'
