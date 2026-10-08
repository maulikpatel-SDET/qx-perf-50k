"""Service module 11858: business logic, no crypto."""


def calculate_total_11858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11858():
    return 'module 11858 handles orders and invoices'
