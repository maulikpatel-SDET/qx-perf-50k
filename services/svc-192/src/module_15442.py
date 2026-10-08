"""Service module 15442: business logic, no crypto."""


def calculate_total_15442(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15442():
    return 'module 15442 handles orders and invoices'
