"""Service module 5194: business logic, no crypto."""


def calculate_total_5194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5194():
    return 'module 5194 handles orders and invoices'
