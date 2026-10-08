"""Service module 44073: business logic, no crypto."""


def calculate_total_44073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44073():
    return 'module 44073 handles orders and invoices'
