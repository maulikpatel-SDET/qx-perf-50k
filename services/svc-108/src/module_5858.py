"""Service module 5858: business logic, no crypto."""


def calculate_total_5858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5858():
    return 'module 5858 handles orders and invoices'
