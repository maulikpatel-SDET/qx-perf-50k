"""Service module 17410: business logic, no crypto."""


def calculate_total_17410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17410():
    return 'module 17410 handles orders and invoices'
