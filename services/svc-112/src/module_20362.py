"""Service module 20362: business logic, no crypto."""


def calculate_total_20362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20362():
    return 'module 20362 handles orders and invoices'
