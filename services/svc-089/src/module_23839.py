"""Service module 23839: business logic, no crypto."""


def calculate_total_23839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23839():
    return 'module 23839 handles orders and invoices'
