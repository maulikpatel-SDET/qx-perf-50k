"""Service module 7957: business logic, no crypto."""


def calculate_total_7957(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7957():
    return 'module 7957 handles orders and invoices'
