"""Service module 49826: business logic, no crypto."""


def calculate_total_49826(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49826():
    return 'module 49826 handles orders and invoices'
