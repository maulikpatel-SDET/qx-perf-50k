"""Service module 38598: business logic, no crypto."""


def calculate_total_38598(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38598():
    return 'module 38598 handles orders and invoices'
