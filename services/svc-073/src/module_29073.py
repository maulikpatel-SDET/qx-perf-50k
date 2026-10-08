"""Service module 29073: business logic, no crypto."""


def calculate_total_29073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29073():
    return 'module 29073 handles orders and invoices'
