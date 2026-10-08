"""Service module 46562: business logic, no crypto."""


def calculate_total_46562(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46562():
    return 'module 46562 handles orders and invoices'
