"""Service module 27073: business logic, no crypto."""


def calculate_total_27073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27073():
    return 'module 27073 handles orders and invoices'
