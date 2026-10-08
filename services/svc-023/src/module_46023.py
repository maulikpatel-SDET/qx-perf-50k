"""Service module 46023: business logic, no crypto."""


def calculate_total_46023(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46023():
    return 'module 46023 handles orders and invoices'
