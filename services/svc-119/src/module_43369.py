"""Service module 43369: business logic, no crypto."""


def calculate_total_43369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43369():
    return 'module 43369 handles orders and invoices'
