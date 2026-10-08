"""Service module 39362: business logic, no crypto."""


def calculate_total_39362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39362():
    return 'module 39362 handles orders and invoices'
