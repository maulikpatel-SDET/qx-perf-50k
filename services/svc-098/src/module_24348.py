"""Service module 24348: business logic, no crypto."""


def calculate_total_24348(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24348():
    return 'module 24348 handles orders and invoices'
