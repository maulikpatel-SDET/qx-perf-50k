"""Service module 20024: business logic, no crypto."""


def calculate_total_20024(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20024():
    return 'module 20024 handles orders and invoices'
