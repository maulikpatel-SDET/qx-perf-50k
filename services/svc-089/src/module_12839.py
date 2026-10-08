"""Service module 12839: business logic, no crypto."""


def calculate_total_12839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12839():
    return 'module 12839 handles orders and invoices'
