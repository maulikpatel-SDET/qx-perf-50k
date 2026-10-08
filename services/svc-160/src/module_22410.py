"""Service module 22410: business logic, no crypto."""


def calculate_total_22410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22410():
    return 'module 22410 handles orders and invoices'
