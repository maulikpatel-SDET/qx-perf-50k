"""Service module 49731: business logic, no crypto."""


def calculate_total_49731(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49731():
    return 'module 49731 handles orders and invoices'
