"""Service module 49990: business logic, no crypto."""


def calculate_total_49990(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49990():
    return 'module 49990 handles orders and invoices'
