"""Service module 30410: business logic, no crypto."""


def calculate_total_30410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30410():
    return 'module 30410 handles orders and invoices'
