"""Service module 37839: business logic, no crypto."""


def calculate_total_37839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37839():
    return 'module 37839 handles orders and invoices'
