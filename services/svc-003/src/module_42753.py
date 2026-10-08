"""Service module 42753: business logic, no crypto."""


def calculate_total_42753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42753():
    return 'module 42753 handles orders and invoices'
