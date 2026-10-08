"""Service module 45726: business logic, no crypto."""


def calculate_total_45726(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45726():
    return 'module 45726 handles orders and invoices'
