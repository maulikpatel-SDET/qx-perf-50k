"""Service module 3623: business logic, no crypto."""


def calculate_total_3623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3623():
    return 'module 3623 handles orders and invoices'
