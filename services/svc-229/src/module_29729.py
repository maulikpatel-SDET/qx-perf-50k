"""Service module 29729: business logic, no crypto."""


def calculate_total_29729(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29729():
    return 'module 29729 handles orders and invoices'
