"""Service module 1409: business logic, no crypto."""


def calculate_total_1409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1409():
    return 'module 1409 handles orders and invoices'
