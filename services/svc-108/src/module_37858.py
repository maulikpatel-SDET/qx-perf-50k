"""Service module 37858: business logic, no crypto."""


def calculate_total_37858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37858():
    return 'module 37858 handles orders and invoices'
