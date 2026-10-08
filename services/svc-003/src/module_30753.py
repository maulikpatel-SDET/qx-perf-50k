"""Service module 30753: business logic, no crypto."""


def calculate_total_30753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30753():
    return 'module 30753 handles orders and invoices'
