"""Service module 19530: business logic, no crypto."""


def calculate_total_19530(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19530():
    return 'module 19530 handles orders and invoices'
