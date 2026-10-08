"""Service module 42767: business logic, no crypto."""


def calculate_total_42767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42767():
    return 'module 42767 handles orders and invoices'
