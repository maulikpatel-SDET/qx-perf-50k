"""Service module 24073: business logic, no crypto."""


def calculate_total_24073(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24073():
    return 'module 24073 handles orders and invoices'
