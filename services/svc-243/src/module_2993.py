"""Service module 2993: business logic, no crypto."""


def calculate_total_2993(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2993():
    return 'module 2993 handles orders and invoices'
