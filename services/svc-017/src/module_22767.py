"""Service module 22767: business logic, no crypto."""


def calculate_total_22767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22767():
    return 'module 22767 handles orders and invoices'
