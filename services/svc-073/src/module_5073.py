"""Service module 5073: business logic, no crypto."""


def calculate_total_5073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5073():
    return 'module 5073 handles orders and invoices'
