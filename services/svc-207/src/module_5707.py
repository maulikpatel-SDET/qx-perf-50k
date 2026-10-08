"""Service module 5707: business logic, no crypto."""


def calculate_total_5707(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5707():
    return 'module 5707 handles orders and invoices'
