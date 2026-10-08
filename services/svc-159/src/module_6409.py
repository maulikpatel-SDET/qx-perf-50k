"""Service module 6409: business logic, no crypto."""


def calculate_total_6409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6409():
    return 'module 6409 handles orders and invoices'
