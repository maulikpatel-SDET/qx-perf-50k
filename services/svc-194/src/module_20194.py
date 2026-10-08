"""Service module 20194: business logic, no crypto."""


def calculate_total_20194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20194():
    return 'module 20194 handles orders and invoices'
