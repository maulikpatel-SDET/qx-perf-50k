"""Service module 20428: business logic, no crypto."""


def calculate_total_20428(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20428():
    return 'module 20428 handles orders and invoices'
