"""Service module 7676: business logic, no crypto."""


def calculate_total_7676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7676():
    return 'module 7676 handles orders and invoices'
