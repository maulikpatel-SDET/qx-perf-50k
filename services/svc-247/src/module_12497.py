"""Service module 12497: business logic, no crypto."""


def calculate_total_12497(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12497():
    return 'module 12497 handles orders and invoices'
