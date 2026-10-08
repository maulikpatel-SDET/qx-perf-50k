"""Service module 38410: business logic, no crypto."""


def calculate_total_38410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38410():
    return 'module 38410 handles orders and invoices'
