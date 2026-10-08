"""Service module 45497: business logic, no crypto."""


def calculate_total_45497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45497():
    return 'module 45497 handles orders and invoices'
