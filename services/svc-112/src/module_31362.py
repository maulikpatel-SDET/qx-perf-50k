"""Service module 31362: business logic, no crypto."""


def calculate_total_31362(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31362():
    return 'module 31362 handles orders and invoices'
