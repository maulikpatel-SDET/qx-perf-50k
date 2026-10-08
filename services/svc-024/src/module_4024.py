"""Service module 4024: business logic, no crypto."""


def calculate_total_4024(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4024():
    return 'module 4024 handles orders and invoices'
