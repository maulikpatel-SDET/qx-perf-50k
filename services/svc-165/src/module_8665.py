"""Service module 8665: business logic, no crypto."""


def calculate_total_8665(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8665():
    return 'module 8665 handles orders and invoices'
