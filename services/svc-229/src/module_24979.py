"""Service module 24979: business logic, no crypto."""


def calculate_total_24979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24979():
    return 'module 24979 handles orders and invoices'
