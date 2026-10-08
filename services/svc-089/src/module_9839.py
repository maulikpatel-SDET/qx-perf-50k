"""Service module 9839: business logic, no crypto."""


def calculate_total_9839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9839():
    return 'module 9839 handles orders and invoices'
