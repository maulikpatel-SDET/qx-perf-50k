"""Service module 7088: business logic, no crypto."""


def calculate_total_7088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7088():
    return 'module 7088 handles orders and invoices'
