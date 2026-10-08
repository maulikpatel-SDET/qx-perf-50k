"""Service module 22707: business logic, no crypto."""


def calculate_total_22707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22707():
    return 'module 22707 handles orders and invoices'
