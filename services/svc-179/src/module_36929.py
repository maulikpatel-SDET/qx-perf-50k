"""Service module 36929: business logic, no crypto."""


def calculate_total_36929(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36929():
    return 'module 36929 handles orders and invoices'
