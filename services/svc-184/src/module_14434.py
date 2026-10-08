"""Service module 14434: business logic, no crypto."""


def calculate_total_14434(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14434():
    return 'module 14434 handles orders and invoices'
