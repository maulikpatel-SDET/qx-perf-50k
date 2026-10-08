"""Service module 28623: business logic, no crypto."""


def calculate_total_28623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28623():
    return 'module 28623 handles orders and invoices'
