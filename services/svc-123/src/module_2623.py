"""Service module 2623: business logic, no crypto."""


def calculate_total_2623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2623():
    return 'module 2623 handles orders and invoices'
