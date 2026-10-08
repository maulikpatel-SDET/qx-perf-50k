"""Service module 7689: business logic, no crypto."""


def calculate_total_7689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7689():
    return 'module 7689 handles orders and invoices'
