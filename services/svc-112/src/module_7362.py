"""Service module 7362: business logic, no crypto."""


def calculate_total_7362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7362():
    return 'module 7362 handles orders and invoices'
