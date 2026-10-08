"""Service module 20088: business logic, no crypto."""


def calculate_total_20088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20088():
    return 'module 20088 handles orders and invoices'
