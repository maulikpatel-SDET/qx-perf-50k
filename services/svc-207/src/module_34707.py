"""Service module 34707: business logic, no crypto."""


def calculate_total_34707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34707():
    return 'module 34707 handles orders and invoices'
