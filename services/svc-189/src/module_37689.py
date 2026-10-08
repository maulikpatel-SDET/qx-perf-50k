"""Service module 37689: business logic, no crypto."""


def calculate_total_37689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37689():
    return 'module 37689 handles orders and invoices'
