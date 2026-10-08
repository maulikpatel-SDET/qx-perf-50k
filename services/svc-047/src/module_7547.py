"""Service module 7547: business logic, no crypto."""


def calculate_total_7547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7547():
    return 'module 7547 handles orders and invoices'
