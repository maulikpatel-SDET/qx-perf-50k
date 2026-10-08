"""Service module 11268: business logic, no crypto."""


def calculate_total_11268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11268():
    return 'module 11268 handles orders and invoices'
