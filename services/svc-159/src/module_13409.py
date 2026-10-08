"""Service module 13409: business logic, no crypto."""


def calculate_total_13409(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13409():
    return 'module 13409 handles orders and invoices'
