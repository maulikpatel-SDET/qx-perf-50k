"""Service module 21469: business logic, no crypto."""


def calculate_total_21469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21469():
    return 'module 21469 handles orders and invoices'
