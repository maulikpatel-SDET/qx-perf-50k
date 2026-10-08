"""Service module 47855: business logic, no crypto."""


def calculate_total_47855(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47855():
    return 'module 47855 handles orders and invoices'
