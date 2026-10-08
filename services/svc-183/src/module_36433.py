"""Service module 36433: business logic, no crypto."""


def calculate_total_36433(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36433():
    return 'module 36433 handles orders and invoices'
