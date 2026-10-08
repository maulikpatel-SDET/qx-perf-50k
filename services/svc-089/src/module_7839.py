"""Service module 7839: business logic, no crypto."""


def calculate_total_7839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7839():
    return 'module 7839 handles orders and invoices'
