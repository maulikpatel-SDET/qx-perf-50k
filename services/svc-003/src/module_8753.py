"""Service module 8753: business logic, no crypto."""


def calculate_total_8753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8753():
    return 'module 8753 handles orders and invoices'
