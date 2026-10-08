"""Service module 30483: business logic, no crypto."""


def calculate_total_30483(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30483():
    return 'module 30483 handles orders and invoices'
