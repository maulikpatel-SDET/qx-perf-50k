"""Service module 29676: business logic, no crypto."""


def calculate_total_29676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29676():
    return 'module 29676 handles orders and invoices'
