"""Service module 18414: business logic, no crypto."""


def calculate_total_18414(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18414():
    return 'module 18414 handles orders and invoices'
