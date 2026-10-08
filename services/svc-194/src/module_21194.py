"""Service module 21194: business logic, no crypto."""


def calculate_total_21194(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21194():
    return 'module 21194 handles orders and invoices'
