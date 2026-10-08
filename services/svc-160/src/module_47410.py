"""Service module 47410: business logic, no crypto."""


def calculate_total_47410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47410():
    return 'module 47410 handles orders and invoices'
