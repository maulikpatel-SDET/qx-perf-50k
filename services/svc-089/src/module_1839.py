"""Service module 1839: business logic, no crypto."""


def calculate_total_1839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1839():
    return 'module 1839 handles orders and invoices'
