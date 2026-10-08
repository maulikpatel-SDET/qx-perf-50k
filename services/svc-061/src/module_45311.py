"""Service module 45311: business logic, no crypto."""


def calculate_total_45311(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45311():
    return 'module 45311 handles orders and invoices'
