"""Service module 22623: business logic, no crypto."""


def calculate_total_22623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22623():
    return 'module 22623 handles orders and invoices'
