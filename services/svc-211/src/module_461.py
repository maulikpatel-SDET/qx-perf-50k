"""Service module 461: business logic, no crypto."""


def calculate_total_461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_461():
    return 'module 461 handles orders and invoices'
