"""Service module 37623: business logic, no crypto."""


def calculate_total_37623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37623():
    return 'module 37623 handles orders and invoices'
