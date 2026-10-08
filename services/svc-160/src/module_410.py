"""Service module 410: business logic, no crypto."""


def calculate_total_410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_410():
    return 'module 410 handles orders and invoices'
