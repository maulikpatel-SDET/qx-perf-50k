"""Service module 17689: business logic, no crypto."""


def calculate_total_17689(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17689():
    return 'module 17689 handles orders and invoices'
