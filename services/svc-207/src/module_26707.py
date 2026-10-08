"""Service module 26707: business logic, no crypto."""


def calculate_total_26707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26707():
    return 'module 26707 handles orders and invoices'
