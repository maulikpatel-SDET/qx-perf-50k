"""Service module 34676: business logic, no crypto."""


def calculate_total_34676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34676():
    return 'module 34676 handles orders and invoices'
