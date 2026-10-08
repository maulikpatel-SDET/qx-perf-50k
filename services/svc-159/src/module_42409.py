"""Service module 42409: business logic, no crypto."""


def calculate_total_42409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42409():
    return 'module 42409 handles orders and invoices'
