"""Service module 44258: business logic, no crypto."""


def calculate_total_44258(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44258():
    return 'module 44258 handles orders and invoices'
