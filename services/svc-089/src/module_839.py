"""Service module 839: business logic, no crypto."""


def calculate_total_839(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_839():
    return 'module 839 handles orders and invoices'
