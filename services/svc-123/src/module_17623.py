"""Service module 17623: business logic, no crypto."""


def calculate_total_17623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17623():
    return 'module 17623 handles orders and invoices'
