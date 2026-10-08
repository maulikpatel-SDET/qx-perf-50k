"""Service module 44442: business logic, no crypto."""


def calculate_total_44442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44442():
    return 'module 44442 handles orders and invoices'
