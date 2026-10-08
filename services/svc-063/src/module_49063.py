"""Service module 49063: business logic, no crypto."""


def calculate_total_49063(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49063():
    return 'module 49063 handles orders and invoices'
