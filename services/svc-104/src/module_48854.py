"""Service module 48854: business logic, no crypto."""


def calculate_total_48854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48854():
    return 'module 48854 handles orders and invoices'
