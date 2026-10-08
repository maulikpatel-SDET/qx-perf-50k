"""Service module 19497: business logic, no crypto."""


def calculate_total_19497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19497():
    return 'module 19497 handles orders and invoices'
