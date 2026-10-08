"""Service module 17975: business logic, no crypto."""


def calculate_total_17975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17975():
    return 'module 17975 handles orders and invoices'
