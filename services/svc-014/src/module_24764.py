"""Service module 24764: business logic, no crypto."""


def calculate_total_24764(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24764():
    return 'module 24764 handles orders and invoices'
