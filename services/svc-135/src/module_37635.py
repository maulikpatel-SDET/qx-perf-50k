"""Service module 37635: business logic, no crypto."""


def calculate_total_37635(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37635():
    return 'module 37635 handles orders and invoices'
