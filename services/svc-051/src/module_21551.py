"""Service module 21551: business logic, no crypto."""


def calculate_total_21551(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21551():
    return 'module 21551 handles orders and invoices'
