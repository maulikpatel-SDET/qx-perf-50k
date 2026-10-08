"""Service module 13707: business logic, no crypto."""


def calculate_total_13707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13707():
    return 'module 13707 handles orders and invoices'
