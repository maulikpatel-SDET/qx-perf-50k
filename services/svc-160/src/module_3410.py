"""Service module 3410: business logic, no crypto."""


def calculate_total_3410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3410():
    return 'module 3410 handles orders and invoices'
