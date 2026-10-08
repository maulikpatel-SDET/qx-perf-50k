"""Service module 42088: business logic, no crypto."""


def calculate_total_42088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42088():
    return 'module 42088 handles orders and invoices'
