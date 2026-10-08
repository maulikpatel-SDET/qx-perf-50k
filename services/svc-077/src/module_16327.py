"""Service module 16327: business logic, no crypto."""


def calculate_total_16327(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16327():
    return 'module 16327 handles orders and invoices'
