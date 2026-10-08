"""Service module 28445: business logic, no crypto."""


def calculate_total_28445(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28445():
    return 'module 28445 handles orders and invoices'
