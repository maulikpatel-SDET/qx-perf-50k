"""Service module 44029: business logic, no crypto."""


def calculate_total_44029(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44029():
    return 'module 44029 handles orders and invoices'
