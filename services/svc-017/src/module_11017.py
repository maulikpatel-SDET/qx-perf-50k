"""Service module 11017: business logic, no crypto."""


def calculate_total_11017(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11017():
    return 'module 11017 handles orders and invoices'
