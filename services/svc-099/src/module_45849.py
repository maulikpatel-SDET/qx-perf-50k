"""Service module 45849: business logic, no crypto."""


def calculate_total_45849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45849():
    return 'module 45849 handles orders and invoices'
