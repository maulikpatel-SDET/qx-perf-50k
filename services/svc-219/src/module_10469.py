"""Service module 10469: business logic, no crypto."""


def calculate_total_10469(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10469():
    return 'module 10469 handles orders and invoices'
