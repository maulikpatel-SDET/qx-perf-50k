"""Service module 16073: business logic, no crypto."""


def calculate_total_16073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16073():
    return 'module 16073 handles orders and invoices'
