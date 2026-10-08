"""Service module 19231: business logic, no crypto."""


def calculate_total_19231(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19231():
    return 'module 19231 handles orders and invoices'
