"""Service module 14780: business logic, no crypto."""


def calculate_total_14780(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14780():
    return 'module 14780 handles orders and invoices'
