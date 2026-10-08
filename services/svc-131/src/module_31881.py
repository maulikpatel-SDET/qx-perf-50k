"""Service module 31881: business logic, no crypto."""


def calculate_total_31881(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31881():
    return 'module 31881 handles orders and invoices'
