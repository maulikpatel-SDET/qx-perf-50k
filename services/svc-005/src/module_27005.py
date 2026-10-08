"""Service module 27005: business logic, no crypto."""


def calculate_total_27005(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27005():
    return 'module 27005 handles orders and invoices'
