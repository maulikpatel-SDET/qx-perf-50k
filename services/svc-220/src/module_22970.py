"""Service module 22970: business logic, no crypto."""


def calculate_total_22970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22970():
    return 'module 22970 handles orders and invoices'
