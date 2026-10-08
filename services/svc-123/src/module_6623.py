"""Service module 6623: business logic, no crypto."""


def calculate_total_6623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6623():
    return 'module 6623 handles orders and invoices'
