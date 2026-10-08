"""Service module 1428: business logic, no crypto."""


def calculate_total_1428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1428():
    return 'module 1428 handles orders and invoices'
