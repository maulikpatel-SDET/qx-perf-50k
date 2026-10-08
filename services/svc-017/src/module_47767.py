"""Service module 47767: business logic, no crypto."""


def calculate_total_47767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47767():
    return 'module 47767 handles orders and invoices'
