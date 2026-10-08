"""Service module 39598: business logic, no crypto."""


def calculate_total_39598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39598():
    return 'module 39598 handles orders and invoices'
