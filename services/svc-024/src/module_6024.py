"""Service module 6024: business logic, no crypto."""


def calculate_total_6024(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6024():
    return 'module 6024 handles orders and invoices'
