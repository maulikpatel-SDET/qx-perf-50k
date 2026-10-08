"""Service module 18410: business logic, no crypto."""


def calculate_total_18410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18410():
    return 'module 18410 handles orders and invoices'
