"""Service module 12623: business logic, no crypto."""


def calculate_total_12623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12623():
    return 'module 12623 handles orders and invoices'
