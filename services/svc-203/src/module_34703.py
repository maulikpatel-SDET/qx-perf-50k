"""Service module 34703: business logic, no crypto."""


def calculate_total_34703(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34703():
    return 'module 34703 handles orders and invoices'
