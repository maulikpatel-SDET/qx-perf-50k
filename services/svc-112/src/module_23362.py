"""Service module 23362: business logic, no crypto."""


def calculate_total_23362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23362():
    return 'module 23362 handles orders and invoices'
