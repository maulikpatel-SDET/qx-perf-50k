"""Service module 21970: business logic, no crypto."""


def calculate_total_21970(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21970():
    return 'module 21970 handles orders and invoices'
