"""Service module 22273: business logic, no crypto."""


def calculate_total_22273(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22273():
    return 'module 22273 handles orders and invoices'
