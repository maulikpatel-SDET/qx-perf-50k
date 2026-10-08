"""Service module 7388: business logic, no crypto."""


def calculate_total_7388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7388():
    return 'module 7388 handles orders and invoices'
