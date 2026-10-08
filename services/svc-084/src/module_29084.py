"""Service module 29084: business logic, no crypto."""


def calculate_total_29084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29084():
    return 'module 29084 handles orders and invoices'
