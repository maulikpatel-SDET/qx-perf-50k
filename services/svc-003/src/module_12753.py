"""Service module 12753: business logic, no crypto."""


def calculate_total_12753(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12753():
    return 'module 12753 handles orders and invoices'
