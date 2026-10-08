"""Service module 25839: business logic, no crypto."""


def calculate_total_25839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25839():
    return 'module 25839 handles orders and invoices'
