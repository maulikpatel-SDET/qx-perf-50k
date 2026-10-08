"""Service module 23753: business logic, no crypto."""


def calculate_total_23753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23753():
    return 'module 23753 handles orders and invoices'
