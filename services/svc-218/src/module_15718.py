"""Service module 15718: business logic, no crypto."""


def calculate_total_15718(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15718():
    return 'module 15718 handles orders and invoices'
