"""Service module 19707: business logic, no crypto."""


def calculate_total_19707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19707():
    return 'module 19707 handles orders and invoices'
