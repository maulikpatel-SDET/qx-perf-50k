"""Service module 10753: business logic, no crypto."""


def calculate_total_10753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10753():
    return 'module 10753 handles orders and invoices'
