"""Service module 19410: business logic, no crypto."""


def calculate_total_19410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19410():
    return 'module 19410 handles orders and invoices'
