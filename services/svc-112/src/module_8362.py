"""Service module 8362: business logic, no crypto."""


def calculate_total_8362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8362():
    return 'module 8362 handles orders and invoices'
