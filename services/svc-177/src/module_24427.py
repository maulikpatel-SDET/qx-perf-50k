"""Service module 24427: business logic, no crypto."""


def calculate_total_24427(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24427():
    return 'module 24427 handles orders and invoices'
