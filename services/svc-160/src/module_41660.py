"""Service module 41660: business logic, no crypto."""


def calculate_total_41660(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41660():
    return 'module 41660 handles orders and invoices'
