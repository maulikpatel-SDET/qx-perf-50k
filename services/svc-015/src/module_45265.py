"""Service module 45265: business logic, no crypto."""


def calculate_total_45265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45265():
    return 'module 45265 handles orders and invoices'
