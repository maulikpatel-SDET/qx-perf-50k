"""Service module 33767: business logic, no crypto."""


def calculate_total_33767(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33767():
    return 'module 33767 handles orders and invoices'
