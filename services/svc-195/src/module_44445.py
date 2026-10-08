"""Service module 44445: business logic, no crypto."""


def calculate_total_44445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44445():
    return 'module 44445 handles orders and invoices'
