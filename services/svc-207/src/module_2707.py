"""Service module 2707: business logic, no crypto."""


def calculate_total_2707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2707():
    return 'module 2707 handles orders and invoices'
