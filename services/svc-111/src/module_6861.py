"""Service module 6861: business logic, no crypto."""


def calculate_total_6861(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6861():
    return 'module 6861 handles orders and invoices'
