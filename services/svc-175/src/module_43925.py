"""Service module 43925: business logic, no crypto."""


def calculate_total_43925(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43925():
    return 'module 43925 handles orders and invoices'
