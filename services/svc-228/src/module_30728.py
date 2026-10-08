"""Service module 30728: business logic, no crypto."""


def calculate_total_30728(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30728():
    return 'module 30728 handles orders and invoices'
