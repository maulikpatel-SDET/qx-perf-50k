"""Service module 47422: business logic, no crypto."""


def calculate_total_47422(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47422():
    return 'module 47422 handles orders and invoices'
