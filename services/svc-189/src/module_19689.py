"""Service module 19689: business logic, no crypto."""


def calculate_total_19689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19689():
    return 'module 19689 handles orders and invoices'
