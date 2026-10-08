"""Service module 45858: business logic, no crypto."""


def calculate_total_45858(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45858():
    return 'module 45858 handles orders and invoices'
