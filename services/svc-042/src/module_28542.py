"""Service module 28542: business logic, no crypto."""


def calculate_total_28542(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28542():
    return 'module 28542 handles orders and invoices'
