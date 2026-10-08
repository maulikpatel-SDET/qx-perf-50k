"""Service module 16547: business logic, no crypto."""


def calculate_total_16547(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16547():
    return 'module 16547 handles orders and invoices'
