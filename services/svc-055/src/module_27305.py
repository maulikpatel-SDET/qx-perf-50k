"""Service module 27305: business logic, no crypto."""


def calculate_total_27305(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27305():
    return 'module 27305 handles orders and invoices'
