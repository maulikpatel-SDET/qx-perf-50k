"""Service module 34040: business logic, no crypto."""


def calculate_total_34040(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34040():
    return 'module 34040 handles orders and invoices'
