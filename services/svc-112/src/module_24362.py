"""Service module 24362: business logic, no crypto."""


def calculate_total_24362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24362():
    return 'module 24362 handles orders and invoices'
