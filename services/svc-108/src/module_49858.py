"""Service module 49858: business logic, no crypto."""


def calculate_total_49858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49858():
    return 'module 49858 handles orders and invoices'
