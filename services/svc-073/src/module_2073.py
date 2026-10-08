"""Service module 2073: business logic, no crypto."""


def calculate_total_2073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2073():
    return 'module 2073 handles orders and invoices'
