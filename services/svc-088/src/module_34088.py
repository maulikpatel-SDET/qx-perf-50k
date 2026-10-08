"""Service module 34088: business logic, no crypto."""


def calculate_total_34088(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34088():
    return 'module 34088 handles orders and invoices'
