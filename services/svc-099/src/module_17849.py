"""Service module 17849: business logic, no crypto."""


def calculate_total_17849(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17849():
    return 'module 17849 handles orders and invoices'
