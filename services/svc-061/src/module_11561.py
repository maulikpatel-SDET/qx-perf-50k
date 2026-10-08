"""Service module 11561: business logic, no crypto."""


def calculate_total_11561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11561():
    return 'module 11561 handles orders and invoices'
