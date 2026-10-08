"""Service module 2839: business logic, no crypto."""


def calculate_total_2839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2839():
    return 'module 2839 handles orders and invoices'
