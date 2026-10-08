"""Service module 12689: business logic, no crypto."""


def calculate_total_12689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12689():
    return 'module 12689 handles orders and invoices'
