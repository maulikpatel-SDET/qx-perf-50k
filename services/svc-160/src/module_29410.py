"""Service module 29410: business logic, no crypto."""


def calculate_total_29410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29410():
    return 'module 29410 handles orders and invoices'
