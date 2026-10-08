"""Service module 37460: business logic, no crypto."""


def calculate_total_37460(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37460():
    return 'module 37460 handles orders and invoices'
