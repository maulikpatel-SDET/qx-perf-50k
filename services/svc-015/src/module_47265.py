"""Service module 47265: business logic, no crypto."""


def calculate_total_47265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47265():
    return 'module 47265 handles orders and invoices'
