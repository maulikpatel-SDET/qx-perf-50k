"""Service module 35855: business logic, no crypto."""


def calculate_total_35855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35855():
    return 'module 35855 handles orders and invoices'
