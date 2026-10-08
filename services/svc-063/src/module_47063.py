"""Service module 47063: business logic, no crypto."""


def calculate_total_47063(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47063():
    return 'module 47063 handles orders and invoices'
