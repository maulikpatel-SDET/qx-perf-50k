"""Service module 46707: business logic, no crypto."""


def calculate_total_46707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46707():
    return 'module 46707 handles orders and invoices'
