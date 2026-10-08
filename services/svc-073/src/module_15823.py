"""Service module 15823: business logic, no crypto."""


def calculate_total_15823(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15823():
    return 'module 15823 handles orders and invoices'
