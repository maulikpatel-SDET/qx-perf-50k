"""Service module 8568: business logic, no crypto."""


def calculate_total_8568(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8568():
    return 'module 8568 handles orders and invoices'
