"""Service module 3362: business logic, no crypto."""


def calculate_total_3362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3362():
    return 'module 3362 handles orders and invoices'
