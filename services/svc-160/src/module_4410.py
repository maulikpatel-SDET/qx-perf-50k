"""Service module 4410: business logic, no crypto."""


def calculate_total_4410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4410():
    return 'module 4410 handles orders and invoices'
