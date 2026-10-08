"""Service module 11362: business logic, no crypto."""


def calculate_total_11362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11362():
    return 'module 11362 handles orders and invoices'
