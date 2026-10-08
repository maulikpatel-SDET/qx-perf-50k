"""Service module 11563: business logic, no crypto."""


def calculate_total_11563(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11563():
    return 'module 11563 handles orders and invoices'
