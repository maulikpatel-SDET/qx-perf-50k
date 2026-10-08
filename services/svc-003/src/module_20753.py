"""Service module 20753: business logic, no crypto."""


def calculate_total_20753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20753():
    return 'module 20753 handles orders and invoices'
