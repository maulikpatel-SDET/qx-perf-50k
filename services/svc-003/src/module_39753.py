"""Service module 39753: business logic, no crypto."""


def calculate_total_39753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39753():
    return 'module 39753 handles orders and invoices'
