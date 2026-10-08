"""Service module 49362: business logic, no crypto."""


def calculate_total_49362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49362():
    return 'module 49362 handles orders and invoices'
