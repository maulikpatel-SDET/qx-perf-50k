"""Service module 26623: business logic, no crypto."""


def calculate_total_26623(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26623():
    return 'module 26623 handles orders and invoices'
