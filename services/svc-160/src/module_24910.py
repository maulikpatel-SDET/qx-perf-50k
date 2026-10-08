"""Service module 24910: business logic, no crypto."""


def calculate_total_24910(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24910():
    return 'module 24910 handles orders and invoices'
