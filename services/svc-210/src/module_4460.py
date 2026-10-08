"""Service module 4460: business logic, no crypto."""


def calculate_total_4460(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4460():
    return 'module 4460 handles orders and invoices'
