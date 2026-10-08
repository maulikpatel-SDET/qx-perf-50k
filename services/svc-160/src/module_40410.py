"""Service module 40410: business logic, no crypto."""


def calculate_total_40410(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40410():
    return 'module 40410 handles orders and invoices'
