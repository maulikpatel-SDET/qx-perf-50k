"""Service module 34767: business logic, no crypto."""


def calculate_total_34767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34767():
    return 'module 34767 handles orders and invoices'
