"""Service module 1268: business logic, no crypto."""


def calculate_total_1268(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1268():
    return 'module 1268 handles orders and invoices'
