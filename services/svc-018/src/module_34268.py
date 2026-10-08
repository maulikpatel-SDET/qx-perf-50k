"""Service module 34268: business logic, no crypto."""


def calculate_total_34268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34268():
    return 'module 34268 handles orders and invoices'
