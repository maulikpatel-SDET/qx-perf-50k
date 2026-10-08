"""Service module 23979: business logic, no crypto."""


def calculate_total_23979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23979():
    return 'module 23979 handles orders and invoices'
