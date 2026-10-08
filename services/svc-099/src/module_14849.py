"""Service module 14849: business logic, no crypto."""


def calculate_total_14849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14849():
    return 'module 14849 handles orders and invoices'
