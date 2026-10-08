"""Service module 28605: business logic, no crypto."""


def calculate_total_28605(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28605():
    return 'module 28605 handles orders and invoices'
