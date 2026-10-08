"""Service module 10815: business logic, no crypto."""


def calculate_total_10815(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10815():
    return 'module 10815 handles orders and invoices'
