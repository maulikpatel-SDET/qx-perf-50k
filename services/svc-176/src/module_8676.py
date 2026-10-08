"""Service module 8676: business logic, no crypto."""


def calculate_total_8676(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8676():
    return 'module 8676 handles orders and invoices'
